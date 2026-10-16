import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import DataLoader, TensorDataset

def get_data(batch_size=256):
    print("Carregando o dataset local...")
    # Carregar do CSV salvo localmente
    df = pd.read_csv('../data/raw/creditcard.csv')
    
    # Extrair features e labels
    y = df['Class'].astype(int).values
    X = df.drop(columns=['Class'])

    
    # Escalar 'Amount'
    scaler = StandardScaler()
    X['Amount'] = scaler.fit_transform(X['Amount'].values.reshape(-1, 1))
    
    # Apenas features
    X = X.values
    
    # Dividir em treino e teste (80/20)
    # Na detecção de anomalia com AE, geralmente treinamos apenas com os dados normais.
    # Por praticidade para a avaliação, usamos o split padrão e depois filtramos o treino.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Filtro: treinar apenas com transações normais (classe 0)
    X_train_normal = X_train[y_train == 0]
    
    # Converter para tensores do PyTorch
    X_train_tensor = torch.tensor(X_train_normal, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32)
    
    train_dataset = TensorDataset(X_train_tensor, X_train_tensor) # Autoencoder entrada = saída
    test_dataset = TensorDataset(X_test_tensor, y_test_tensor) # Aqui a saída é a label para avaliação
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader, X_train_normal.shape[1]
