import random

def simular_aluno(com_extensao):
    erros_estruturais = []
    erro_base = 4 # Quantidade de erros estruturais na Tarefa 1
    
    for tarefa in range(1, 6):
        if com_extensao:
            # Com a extensão, simulamos que a reflexão forçada derruba os erros
            erro_atual = max(0, erro_base - (tarefa - 1))
        else:
            # Sem a extensão (jeito de hoje), o erro se mantém constante ou cai muito pouco
            erro_atual = erro_base - random.randint(0, 1)
            
        erros_estruturais.append(erro_atual)
    return erros_estruturais

print("| Condição | T1 | T2 | T3 | T4 | T5 | Total de Erros | Redução T1->T5 |")
print("|:---|---:|---:|---:|---:|---:|---:|---:|")

# Condição A: Jeito de Hoje (Sem Rastro Cognitivo)
random.seed(42) # Para manter o resultado determinístico
erros_a = simular_aluno(com_extensao=False)
reducao_a = erros_a[0] - erros_a[-1]

# Condição B: Com Rastro Cognitivo
erros_b = simular_aluno(com_extensao=True)
reducao_b = erros_b[0] - erros_b[-1]

print(f"| A: Sem a Extensão | {erros_a[0]} | {erros_a[1]} | {erros_a[2]} | {erros_a[3]} | {erros_a[4]} | {sum(erros_a)} | {reducao_a} erros |")
print(f"| B: Com a Extensão | {erros_b[0]} | {erros_b[1]} | {erros_b[2]} | {erros_b[3]} | {erros_b[4]} | {sum(erros_b)} | {reducao_b} erros |")