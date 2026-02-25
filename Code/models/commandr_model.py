import os
import cohere
from models.model_interface import LLMModel

class CommandRModel(LLMModel):
    """CommandR model implementation"""
    
    def __init__(self, model_name: str = "command-a-03-2025"):
        super().__init__(model_name)
        self.api_key = os.getenv("COMMANDR_API_KEY")
        if self.api_key:
            self.co = cohere.ClientV2(self.api_key)
        else:
            self.co = None
    
    def generate_response(self, prompt: str) -> str:
        """Generate code from a prompt using CommandR"""
        if not self.is_available():
            return "CommandR model not available - missing API key"
        
        try:
            response = self.co.chat(
                model=self.name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.message.content[0].text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def is_available(self) -> bool:
        """Check if CommandR API key is available"""
        return bool(self.api_key) 