import random
import math
import asyncio
from typing import List, Dict
from models.model_interface import LLMModel

class LLMAgent:
    """Main agent class that manages multiple LLM models"""
    
    def __init__(self):
        self.models_dict = {}
        self.secretary_model_judge = None  # The model that will judge code quality
        self.secretary_candidates = [] # The models that will be candidates for the best model
        self.secretary_ratio = 1/math.e  # ≈ 0.368 
        self.models_responses = {}
        self.best_model = None
        self.learning_size = 0

    def add_model(self, model: LLMModel):
        """Add a new model to the agent"""
        self.models_dict[model.name] = model
        self.secretary_candidates.append(model.name)
        self.learning_size = max(1, math.ceil((len(self.secretary_candidates) - 1) * self.secretary_ratio))
    
    async def generate_response_with_model(self, model_name: str, guidance: str, prompt: str) -> str:
        """Generate code with a specific model by name"""
        model = self.models_dict[model_name]
        if model.is_available():
            prompt = f"""{guidance}

            Prompt:
            {prompt}
            """
            try:
                return model.generate_response(prompt)
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return f"Model {model_name} is not available"
    

    def judge_with_model(self, model_name: str, code1: str, code2: str, guidance: str) -> int:
        # Validate inputs
        if not model_name or not code1 or not code2 or not guidance:
            raise ValueError("All parameters must be non-empty")
        
        # Get the model
        model = self.models_dict[model_name]
        if not model.is_available():
            raise ValueError(f"Model {model_name} is not available")
        
        prompt = f"""{guidance}

        Code 1:
        {code1}

        Code 2:
        {code2}
        
        IMPORTANT: You must respond with ONLY the number '1' or '2'. No other text."""

        try:
            response = model.generate_response(prompt)
            if "1" in response or "first" in response.lower():
                return 1
            elif "2" in response or "second" in response.lower():
                return 2
            else:
                raise ValueError(f"Unclear response: {response}")
        except Exception as e:
            raise RuntimeError(f"Failed to judge with model '{model_name}': {str(e)}")


    def update_secretary(self):
        # Get all model names and shuffle them
        random.shuffle(self.secretary_candidates)

        total_models = len(self.secretary_candidates)
        
        if total_models < 2:
            raise ValueError("Need at least 2 models for secretary algorithm: 1 judge + 1 learning model")   
        
        # First model becomes the judge
        self.secretary_model_judge = self.secretary_candidates[0]

    async def run_create_phase(self, prompt_create_code: str, prompt: str) -> None:
        """Generate code with all learning models in parallel"""
        # Clear previous results
        self.models_responses = {}
        self.best_model = None
        
        # Run all models in parallel
        tasks = [self.generate_response_with_model(model_name, prompt_create_code, prompt) 
                 for model_name in self.secretary_candidates[1:]]
        results = await asyncio.gather(*tasks)
        
        # Store results
        for i, model_name in enumerate(self.secretary_candidates[1:]):
            self.models_responses[model_name] = results[i]

    def run_judge_phase(self, prompt_judge: str) -> None:
        """Select best code through pairwise comparison"""
        # Select best code through pairwise comparison
        self.best_model = self.secretary_candidates[1]
        best_code = self.models_responses[self.best_model]
        
        # Check if we have enough models to compare
        if len(self.secretary_candidates) < 3:
            return  # Not enough models to compare
        
        for i, model_name in enumerate(self.secretary_candidates[2:], start=2):
            current_code = self.models_responses[model_name]
            result = self.judge_with_model(self.secretary_model_judge, best_code, current_code, prompt_judge)
            
            if result == 2:  # Current model is better
                self.best_model = model_name
                best_code = current_code
                
                # Check if model is beyond 1/e threshold
                if i >= 1 + self.learning_size:
                    break  # Stop and keep this model
            
            # If we reached the last model, keep it
            if i == len(self.secretary_candidates) - 1:
                self.best_model = model_name
                break
                
    