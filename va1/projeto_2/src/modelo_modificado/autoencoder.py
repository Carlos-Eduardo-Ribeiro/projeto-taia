import torch
import torch.nn as nn

class ModifiedAutoencoder(nn.Module):
    def __init__(self, input_dim):
        super(ModifiedAutoencoder, self).__init__()
        
        # Encoder Modificado: LeakyReLU, BatchNorm, Dropout
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.BatchNorm1d(32),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.1),
            
            nn.Linear(32, 16),
            nn.BatchNorm1d(16),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.1),
            
            nn.Linear(16, 8),
            nn.BatchNorm1d(8),
            nn.LeakyReLU(0.2)
        )
        
        # Decoder Modificado
        self.decoder = nn.Sequential(
            nn.Linear(8, 16),
            nn.BatchNorm1d(16),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.1),
            
            nn.Linear(16, 32),
            nn.BatchNorm1d(32),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.1),
            
            nn.Linear(32, input_dim),
            nn.Identity()
        )
        
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
