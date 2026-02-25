import json
import os
import ast
from agent.llm_agent import LLMAgent
from models.openai_model import OpenAIModel
from models.claude_model import ClaudeModel
from models.gemini_model import GeminiModel
from models.deepseek_model import DeepSeekModel
from models.mistral_model import MistralModel
from models.commandr_model import CommandRModel
# Guidance texts are imported but not currently used in the basic implementation
# from guidance_texts import WRITE_GUIDANCE_HARD, WRITE_GUIDANCE_EASY, JUDGE_GUIDANCE_HARD, JUDGE_GUIDANCE_EASY

class LLMSystem:
    """Main system class for managing LLM code generation"""
    
    def __init__(self):
        # Create agent with models
        self.agent = LLMAgent()
        self.agent.add_model(OpenAIModel())
        self.agent.add_model(ClaudeModel())
        self.agent.add_model(GeminiModel())
        self.agent.add_model(DeepSeekModel())
        self.agent.add_model(MistralModel())
        self.agent.add_model(CommandRModel())
        
        # Current prompt and response fields
        self.current_prompt = None    
        

    def save_session_results(self, prompt: str, create_guidance: str, judge_guidance: str, question_id=None):

        session_dir = f"history/{question_id}"

        # Create subdirectory for this combination
        combo_name = f"{create_guidance}_{judge_guidance}".replace("_GUIDANCE_", "_")
        combo_dir = f"{session_dir}/{combo_name}"
        os.makedirs(combo_dir, exist_ok=True)
        
        # Save codes (only raw model code as-is, no headers/prompts, no modifications)
        for model_name, code in self.agent.models_responses.items():
            safe_name = model_name.replace("-", "_").replace(" ", "_")
            with open(f"{combo_dir}/{safe_name}_code.py", "w") as f:
                f.write(code or "")
        
        # Evaluate pass rate using the saved Python file of the winning model
        best_model_safe = (self.agent.best_model or "").replace("-", "_").replace(" ", "_")
        best_code_path = os.path.join(combo_dir, f"{best_model_safe}_code.py")
        best_code_text = ""
        if os.path.exists(best_code_path):
            try:
                with open(best_code_path, "r") as bf:
                    best_code_text = bf.read()
            except Exception:
                best_code_text = self.agent.models_responses.get(self.agent.best_model, "")
        else:
            best_code_text = self.agent.models_responses.get(self.agent.best_model, "")

        # Normalize leading/trailing markdown fences if the file starts with a fenced block
        if isinstance(best_code_text, str):
            stripped_file = best_code_text.lstrip()
            if stripped_file.startswith("```"):
                lines = stripped_file.splitlines()
                # drop the first fence line (possibly with language)
                if lines:
                    lines = lines[1:]
                # drop trailing fence line if present
                if lines and lines[-1].strip() == "```":
                    lines = lines[:-1]
                best_code_text = "\n".join(lines)

        pass_rate = self.evaluate_pass_rate(question_id, best_code_text)

        # Save best model metadata (without embedding code)
        best_payload = {
            "best_model": self.agent.best_model,
            "pass_rate": pass_rate
        }
        with open(f"{combo_dir}/best_model.json", "w") as f:
            json.dump(best_payload, f, indent=2)
        
        # Save session metadata
        session_data = {
            "prompt": prompt,
            "secretary_judge": self.agent.secretary_model_judge,
            "learning_size": self.agent.learning_size,
            "all_candidates": self.agent.secretary_candidates,
        }
        
        with open(f"{session_dir}/session_data.json", "w") as f:
            json.dump(session_data, f, indent=2)
        
    def evaluate_pass_rate(self, question_id, code_text: str) -> float:
        """Simple evaluator: find question by id, run examples, compute pass ratio."""
        try:
            qpath = os.path.join("questions", "competition.json")
            if not question_id or not os.path.exists(qpath):
                return 0.0

            # Locate question object
            target = None
            with open(qpath, "r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    obj = json.loads(line)
                    if obj.get("id") == question_id:
                        target = obj
                        break
            if not target:
                return 0.0
            examples = target.get("input_output") or []
            if not examples:
                return 0.0

            # Sanitize possible markdown fences
            if isinstance(code_text, str):
                stripped_eval = code_text.strip()
                if stripped_eval.startswith("```"):
                    stripped_eval = "\n".join(stripped_eval.splitlines()[1:])
                if stripped_eval.endswith("```"):
                    stripped_eval = "\n".join(stripped_eval.splitlines()[:-1])
            else:
                stripped_eval = ""

            # Parse code and get all functions
            try:
                module = ast.parse(stripped_eval)
                all_functions = [n.name for n in module.body if isinstance(n, ast.FunctionDef)]
            except Exception:
                return 0.0
            
            if not all_functions:
                return 0.0

            # Execute code
            ns = {}
            exec(stripped_eval, ns)

            # Try each function and find the maximum pass rate
            max_pass_rate = 0.0
            total = len(examples)
            
            for func_name in all_functions:
                try:
                    fn = ns.get(func_name)
                    if not callable(fn):
                        continue
                    
                    # Test this function on all examples
                    passed = 0
                    for ex in examples:
                        inp = ex.get("input")
                        expected = ex.get("output")
                        args = inp if isinstance(inp, list) else [inp]
                        res = fn(*args)
                        exp = expected[0] if isinstance(expected, list) and len(expected) == 1 else expected
                        if res == exp or str(res) == str(exp):
                            passed += 1
                    
                    # Calculate pass rate for this function
                    if total > 0:
                        func_pass_rate = passed / total
                        max_pass_rate = max(max_pass_rate, func_pass_rate)
                        
                except Exception:
                    continue
            
            return max_pass_rate
        except Exception:
            return 0.0