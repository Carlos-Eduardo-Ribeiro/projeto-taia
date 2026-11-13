import warnings
import json
import time
import urllib.request
warnings.filterwarnings("ignore")

# --- CONSERTO DO PyAV (mantido) ---
import av
_original_open = av.open
def conserto_av_open(*args, **kwargs):
    kwargs.pop('metadata_errors', None)
    return _original_open(*args, **kwargs)
av.open = conserto_av_open
# ----------------------------------

from faster_whisper import WhisperModel

inicio_total = time.perf_counter()

# 1. NOVA ENTRADA: Áudio do aluno justificando o código
arquivo_audio = "explicacao.mp4" # Se o seu áudio for .m4a ou .wav, mude aqui

print("Ouvindo a justificativa do aluno...")
inicio_whisper = time.perf_counter()
model = WhisperModel("small", device="cpu", compute_type="int8")
segments, _ = model.transcribe(arquivo_audio, beam_size=5)

texto_aluno = "".join([segment.text for segment in segments]).strip()
tempo_whisper = time.perf_counter() - inicio_whisper
print(f"Transcrição: {texto_aluno}")

# 2. NOVA SAÍDA: Avaliação semântica via Ollama (Qwen2.5-Coder)
print("\nAvaliando a compreensão da arquitetura...")
inicio_qwen = time.perf_counter()
prompt = f"O aluno justificou a alteração no código com a seguinte frase: '{texto_aluno}'. Avalie em apenas 1 frase curta se ele parece entender de programação ou se está falando bobagem."

req = urllib.request.Request("http://localhost:11434/api/generate", method="POST")
req.add_header('Content-Type', 'application/json')
dados = json.dumps({"model": "qwen2.5-coder:1.5b", "prompt": prompt, "stream": False}).encode('utf-8')

try:
    resposta = urllib.request.urlopen(req, data=dados)
    resultado = json.loads(resposta.read().decode('utf-8'))
    print(f"Veredito do Rastro Cognitivo: {resultado['response']}")
except Exception as e:
    print(f"Erro ao conectar com Ollama: {e}")

tempo_qwen = time.perf_counter() - inicio_qwen
tempo_total = time.perf_counter() - inicio_total
print(f"\nTempo de execução: {tempo_total:.2f}s (Whisper: {tempo_whisper:.2f}s | Qwen: {tempo_qwen:.2f}s)")