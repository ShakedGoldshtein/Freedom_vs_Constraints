import os
import requests
from models.model_interface import LLMModel

class DeepSeekModel(LLMModel):
    """DeepSeek model implementation"""
    
    def __init__(self, model_name: str = "deepseek-chat"):
        super().__init__(model_name)
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
    
    def generate_response(self, prompt: str) -> str:
        """Generate code from a prompt using DeepSeek"""
        if not self.is_available():
            return "DeepSeek model not available - missing API key"
        
        code_prompt = f"Please generate code for the following request. Return only the code without explanations:\n\n{prompt}"
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": self.name,
                "messages": [{"role": "user", "content": code_prompt}],
                "max_tokens": 1000,
                "temperature": 0.7
            }
            
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def is_available(self) -> bool:
        """Check if DeepSeek API key is available"""
        return bool(self.api_key) 