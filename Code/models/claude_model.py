import os
import anthropic
from models.model_interface import LLMModel

class ClaudeModel(LLMModel):
    """Claude model implementation"""
    
    def __init__(self, model_name: str = "claude-3-5-sonnet-20241022"):
        super().__init__(model_name)
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        else:
            self.client = None
    
    def generate_response(self, prompt: str) -> str:
        """Generate code from a prompt using Claude"""
        if not self.is_available():
            return "Claude model not available - missing API key"
        
        code_prompt = f"Please generate code for the following request. Return only the code without explanations:\n\n{prompt}"
        
        try:
            response = self.client.messages.create(
                model=self.name,
                max_tokens=1000,
                messages=[{"role": "user", "content": code_prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def is_available(self) -> bool:
        """Check if Claude API key is available"""
        return bool(self.api_key) and self.client is not None 