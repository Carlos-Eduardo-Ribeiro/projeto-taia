"""Caminhos globais do projeto e parâmetros fixos.

Centraliza a localização dos datasets brutos e dos artefatos processados
para que módulos, notebooks e a aplicação Streamlit use sempre os mesmos
caminhos relativos à raiz do projeto.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

HEART_PATH = DATA_RAW / "heart.csv"
DIABETIC_PATH = DATA_RAW / "diabetic_data.csv"
IDS_MAPPING_PATH = DATA_RAW / "IDS_mapping.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.2  # split obrigatório 80% treino / 20% teste