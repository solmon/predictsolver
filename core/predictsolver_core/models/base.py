import torch
import torch.nn as nn

class BaseModel(nn.Module):
    """Base model class for all predictive models in the predictsolver package."""
    
    def __init__(self):
        super().__init__()
        self.model_name = "base_model"
        
    def save(self, path):
        """Save model weights to disk."""
        torch.save(self.state_dict(), path)
        
    def load(self, path):
        """Load model weights from disk."""
        self.load_state_dict(torch.load(path))
        
    def summary(self):
        """Return a summary of the model."""
        return f"{self.model_name}: {sum(p.numel() for p in self.parameters())} parameters"
