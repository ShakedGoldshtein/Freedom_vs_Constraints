import os
import openai
from models.model_interface import LLMModel

class OpenAIModel(LLMModel):
    """OpenAI model implementation"""
    
    def __init__(self, model_name: str = "gpt-4"):
        super().__init__(model_name)
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key:
            openai.api_key = self.api_key
        else:
            openai.api_key = None
    
    def generate_response(self, prompt: str) -> str:
        """Generate code from a prompt using OpenAI"""
        if not self.is_available():
            return "OpenAI model not available - missing API key"
        
        code_prompt = f"Please generate code for the following request. Return only the code without explanations:\n\n{prompt}"
        
        try:
            response = openai.chat.completions.create(
                model=self.name,
                messages=[{"role": "user", "content": code_prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def is_available(self) -> bool:
        """Check if OpenAI API key is available"""
        return bool(self.api_key) 