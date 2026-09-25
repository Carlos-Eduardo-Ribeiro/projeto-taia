import os
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score
import matplotlib.pyplot as plt

from dataset import get_data
from modelo_original.autoencoder import SimpleAutoencoder
from modelo_modificado.autoencoder import ModifiedAutoencoder

def train_and_evaluate(model_type, epochs=20, batch_size=256, lr=1e-3):
    print(f"--- Iniciando experimento com o modelo: {model_type} ---")
    
    # 1. Obter dados
    train_loader, test_loader, input_dim = get_data(batch_size=batch_size)
    
    # 2. Instanciar modelo
    if model_type == 'original':
        model = SimpleAutoencoder(input_dim)
        save_dir = '../results/original'
    else:
        model = ModifiedAutoencoder(input_dim)
        save_dir = '../results/modified'
        
    os.makedirs(save_dir, exist_ok=True)
    
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    # 3. Loop de Treinamento
    train_losses = []
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for data, _ in train_loader:
            optimizer.zero_grad()
            reconstructed = model(data)
            loss = criterion(reconstructed, data)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            
        avg_loss = epoch_loss / len(train_loader)
        train_losses.append(avg_loss)
        print(f"Epoch [{epoch+1}/{epochs}] Loss: {avg_loss:.4f}")
        
    # Salvar modelo
    torch.save(model.state_dict(), os.path.join(save_dir, 'model.pth'))
    
    # Plotar curva de loss
    plt.figure()
    plt.plot(range(1, epochs+1), train_losses, marker='o', label='Train Loss')
    plt.title(f'Loss de Treinamento - {model_type.capitalize()}')
    plt.xlabel('Época')
    plt.ylabel('MSE Loss')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'loss_curve.png'))
    plt.close()
    
    # 4. Avaliação (Inferência)
    model.eval()
    errors = []
    labels = []
    
    with torch.no_grad():
        for data, target in test_loader:
            reconstructed = model(data)
            # Calcular o erro de reconstrução por amostra
            mse = torch.mean((data - reconstructed) ** 2, dim=1).numpy()
            errors.extend(mse)
            labels.extend(target.numpy())
            
    errors = np.array(errors)
    labels = np.array(labels)
    
    # Definir um threshold
    # Como as anomalias são fraude (label=1), e têm maior erro, pegamos um percentil 
    # Por ex, se a taxa de fraude é ~0.17%, podemos colocar o threshold no percentil 99.8 das normais
    # Para ser simples, vamos calcular o threshold como media + 3*std dos erros nos dados normais do teste
    normal_errors = errors[labels == 0]
    threshold = np.mean(normal_errors) + 3 * np.std(normal_errors)
    
    # Predições
    preds = (errors > threshold).astype(int)
    
    # Calcular métricas
    precision = precision_score(labels, preds)
    recall = recall_score(labels, preds)
    f1 = f1_score(labels, preds)
    roc_auc = roc_auc_score(labels, errors)
    acc = accuracy_score(labels, preds)
    
    print("\nResultados:")
    print(f"Threshold: {threshold:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")
    print(f"Accuracy: {acc:.4f}\n")
    
    # Salvar métricas
    with open(os.path.join(save_dir, 'metrics.txt'), 'w') as f:
        f.write(f"Threshold: {threshold:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall: {recall:.4f}\n")
        f.write(f"F1-Score: {f1:.4f}\n")
        f.write(f"ROC-AUC: {roc_auc:.4f}\n")
        f.write(f"Accuracy: {acc:.4f}\n")
        
    # Plotar distribuição do erro de reconstrução
    plt.figure(figsize=(10, 6))
    plt.hist(normal_errors, bins=50, alpha=0.6, color='blue', label='Normal', density=True)
    fraud_errors = errors[labels == 1]
    plt.hist(fraud_errors, bins=50, alpha=0.6, color='red', label='Fraude', density=True)
    plt.axvline(threshold, color='black', linestyle='dashed', linewidth=2, label='Threshold')
    plt.title(f'Distribuição do Erro de Reconstrução - {model_type.capitalize()}')
    plt.xlabel('MSE Reconstrução')
    plt.ylabel('Densidade')
    plt.yscale('log') # Escala log ajuda a ver melhor as caudas
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'error_distribution.png'))
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Treina e avalia o AE original ou modificado.")
    parser.add_argument("--model", type=str, choices=['original', 'modified'], required=True, help="Modelo a ser treinado")
    parser.add_argument("--epochs", type=int, default=15, help="Número de épocas")
    args = parser.parse_args()
    
    train_and_evaluate(args.model, epochs=args.epochs)
