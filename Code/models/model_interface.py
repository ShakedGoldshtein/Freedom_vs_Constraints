from abc import ABC, abstractmethod

class LLMModel(ABC):
    """Base interface for all LLM models"""
    
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate code from a prompt"""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if the model is available"""
        pass 