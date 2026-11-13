import time
import requests
import json

# Dados simulados do piloto (Transcrição + AST) e o Gabarito (se deveria Passar ou Barrar)
testes = [
    {
        "id": "T1",
        "ast": "class Database { private static instance; }",
        "transcricao": "Usei o padrão singleton para não abrir um monte de conexão e estourar a memória.",
        "gabarito": "Passar"
    },
    {
        "id": "T2", # Simulando um erro do Whisper (sotaque/ruído)
        "ast": "class Database { private static instance; }",
        "transcricao": "Usei o cicloton para não abrir conecção e estore a memória.",
        "gabarito": "Passar"
    },
    {
        "id": "T3", # Aluno falando bobagem/enrolando
        "ast": "class Database { private static instance; }",
        "transcricao": "Eu fiz assim porque o professor mandou e o código ficou mais bonito na tela.",
        "gabarito": "Barrar"
    },
    {
        "id": "T4", # Ablação: Sem AST (O modelo não sabe o que o aluno codou)
        "ast": "NENHUMA - ABLAÇÃO",
        "transcricao": "Usei o padrão singleton para não abrir um monte de conexão.",
        "gabarito": "Passar"
    }
]

url = "http://localhost:11434/api/generate"
modelo = "qwen2.5-coder:1.5b" # O modelo que você usou no tec

print(f"| ID | Condição | Tempo (s) | Gabarito | Qwen | Resultado |")
print(f"|:---|:---|---:|:---|:---|:---|")

for t in testes:
    prompt = f"O aluno fez o seguinte código (AST): {t['ast']}. A justificativa dele por voz foi transcrita como: '{t['transcricao']}'. Ele entende o motivo técnico da mudança? Responda APENAS 'Passar' ou 'Barrar'."
    
    inicio = time.time()
    try:
        payload = {"model": modelo, "prompt": prompt, "stream": False, "temperature": 0.0}
        resposta = requests.post(url, json=payload).json()
        qwen_resposta = resposta.get("response", "").strip()
        # Limpando a resposta do LLM para pegar só a palavra chave
        qwen_veredito = "Passar" if "Passar" in qwen_resposta else "Barrar" if "Barrar" in qwen_resposta else "Confuso"
    except Exception as e:
        qwen_veredito = "Erro API"
    fim = time.time()
    
    tempo_decorrido = round(fim - inicio, 2)
    
    # Avaliando as métricas
    if qwen_veredito == t['gabarito']:
        resultado = "✅ Acerto"
    elif qwen_veredito == "Passar" and t['gabarito'] == "Barrar":
        resultado = "❌ Falso Positivo"
    elif qwen_veredito == "Barrar" and t['gabarito'] == "Passar":
        resultado = "❌ Falso Negativo"
    else:
        resultado = "⚠️ Erro"
        
    condicao = "Sem AST" if t['ast'] == "NENHUMA - ABLAÇÃO" else "Whisper Ruim" if t['id'] == "T2" else "Normal"
    
    print(f"| {t['id']} | {condicao} | {tempo_decorrido} | {t['gabarito']} | {qwen_veredito} | {resultado} |")