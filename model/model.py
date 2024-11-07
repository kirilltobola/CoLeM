import torch.nn as nn
from transformers import AutoConfig, AutoModel

class Colem(nn.Module):
    """TODO"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO move from here:
        pretrained_model_name = "bert-base-uncased"
        latent_space_dim = 128

        self.config = AutoConfig.from_pretrained(pretrained_model_name)

        self.encoder = AutoModel.from_pretrained(pretrained_model_name)
        self.projector = nn.Sequential(
            nn.Linear(in_features=self.config.hidden_size, out_features=self.config.hidden_size),
            nn.ReLU(),
            nn.Linear(in_features=self.config.hidden_size, out_features=latent_space_dim)
        )

    def forward(self):
        """TODO"""
        pass


if __name__ == "__main__":
    model = Colem()
    print(model)
