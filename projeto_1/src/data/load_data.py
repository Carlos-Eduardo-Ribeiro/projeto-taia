"""Funções de leitura dos datasets brutos.

O arquivo IDS_mapping.csv não é uma tabela única: ele contém três dicionários
separados por linhas em branco (admission_type_id, discharge_disposition_id e
admission_source_id). Cada seção é convertida em um dicionário {id: descrição}.
"""

from pathlib import Path

import pandas as pd

from src.config import HEART_PATH, IDS_MAPPING_PATH, DIABETIC_PATH


def load_heart(path: Path | str = HEART_PATH) -> pd.DataFrame:
    """Retorna o dataset Heart Disease (heart.csv)."""
    return pd.read_csv(path)


def load_diabetic(path: Path | str = DIABETIC_PATH) -> pd.DataFrame:
    """Retorna o dataset Diabetes 130-US Hospitals (diabetic_data.csv)."""
    return pd.read_csv(path, low_memory=False)


SECTION_NAMES = [
    "admission_type_id",
    "discharge_disposition_id",
    "admission_source_id",
]


def load_ids_mapping(path: Path | str = IDS_MAPPING_PATH) -> dict[str, dict[str, str]]:
    """Lê o IDS_mapping.csv e agrupa as descrições por seção.

    O arquivo possui três blocos com o formato:
        <nome_da_secao>,description
        <id>,<descrição>
    separados por linhas em branco.

    Retorna algo como:
        {"admission_type_id": {"1": "Emergency", ...},
         "discharge_disposition_id": {...},
         "admission_source_id": {...}}
    """
    texto = pd.read_csv(path, header=None, sep=",", keep_default_na=False)
    secoes: dict[str, dict[str, str]] = {}
    secao_atual: str | None = None
    for _, linha in texto.iterrows():
        chave = str(linha[0]).strip()
        valor = str(linha[1]) if len(linha) > 1 else ""
        if chave in SECTION_NAMES and chave not in secoes:
            secao_atual = chave
            secoes[secao_atual] = {}
            continue
        if chave in SECTION_NAMES:
            continue
        if chave == "":
            continue
        if secao_atual is not None:
            secoes[secao_atual][chave] = valor.strip()
    return secoes