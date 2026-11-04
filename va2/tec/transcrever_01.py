import warnings
warnings.filterwarnings("ignore")

# --- INÍCIO DO CONSERTO (Patch para o erro da biblioteca PyAV) ---
import av
_original_open = av.open
def conserto_av_open(*args, **kwargs):
    kwargs.pop('metadata_errors', None) # Remove o parâmetro problemático antes de quebrar
    return _original_open(*args, **kwargs)
av.open = conserto_av_open
# --- FIM DO CONSERTO ---

from faster_whisper import WhisperModel

model_size = "small"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("jfk.flac", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))