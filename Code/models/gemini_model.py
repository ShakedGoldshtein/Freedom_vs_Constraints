import os
import google.generativeai as genai
from models.model_interface import LLMModel

class GeminiModel(LLMModel):
    """Gemini model implementation"""
    
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        super().__init__(model_name)
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(model_name)
        else:
            self.model = None
    
    def generate_response(self, prompt: str) -> str:
        """Generate code from a prompt using Gemini"""
        if not self.is_available():
            return "Gemini model not available - missing API key"
        
        code_prompt = f"Please generate code for the following request. Return only the code without explanations:\n\n{prompt}"
        
        try:
            response = self.model.generate_content(code_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def is_available(self) -> bool:
        """Check if Gemini API key is available"""
        return bool(self.api_key) and self.model is not None 