"""Pré-processamento das bases do projeto.

Todos os tratamentos são feitos com pandas e numpy (sem sklearn). O split
80/20 é feito manualmente e a padronização (z-score) é ajustada apenas na
parte de treino e aplicada também no teste, para não haver vazamento de dados.
"""

import numpy as np
import pandas as pd

from src.config import RANDOM_STATE, TEST_SIZE

# --------------------------------------------------------------------------- #
# Split 80/20
# --------------------------------------------------------------------------- #


def split_train_test(
    X: pd.DataFrame | np.ndarray,
    y: pd.Series | np.ndarray,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> tuple:
    """Divide os dados em 80% treino / 20% teste (parâmetro obrigatório)."""
    rng = np.random.default_rng(random_state)
    n = len(X)
    indices = rng.permutation(n)
    n_test = int(round(n * test_size))
    test_idx = indices[:n_test]
    train_idx = indices[n_test:]
    return X.iloc[train_idx] if hasattr(X, "iloc") else X[train_idx], (
        X.iloc[test_idx] if hasattr(X, "iloc") else X[test_idx]
    ), y.iloc[train_idx] if hasattr(y, "iloc") else y[train_idx], (
        y.iloc[test_idx] if hasattr(y, "iloc") else y[test_idx]
    )


# --------------------------------------------------------------------------- #
# Padronização (standardization / z-score)
# --------------------------------------------------------------------------- #


class StandardScaler:
    """Padronização manual: (x - média) / desvio padrão."""

    def __init__(self):
        self.mean_: np.ndarray | None = None
        self.std_: np.ndarray | None = None

    def fit(self, X: np.ndarray | pd.DataFrame) -> "StandardScaler":
        X = np.asarray(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        self.mean_ = X.mean(axis=0)
        self.std_ = X.std(axis=0)
        self.std_[self.std_ == 0] = 1.0  # evita divisão por zero
        return self

    def transform(self, X: np.ndarray | pd.DataFrame) -> np.ndarray:
        X = np.asarray(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return (X - self.mean_) / self.std_

    def fit_transform(self, X: np.ndarray | pd.DataFrame) -> np.ndarray:
        return self.fit(X).transform(X)


# --------------------------------------------------------------------------- #
# Tratamento de outliers (winsorização por IQR ou z-score)
# --------------------------------------------------------------------------- #


def clip_outliers(
    X: pd.DataFrame,
    columns: list[str],
    method: str = "iqr",
    multiplier: float = 1.5,
    z_threshold: float = 4.0,
) -> pd.DataFrame:
    """Limita valores extremos nas colunas indicadas.

    method="iqr": corta em Q1 - k*IQR e Q3 + k*IQR.
    method="zscore": corta em |z| > z_threshold.
    """
    X = X.copy()
    for col in columns:
        s = X[col]
        if method == "iqr":
            q1, q3 = s.quantile(0.25), s.quantile(0.75)
            iqr = q3 - q1
            lo, hi = q1 - multiplier * iqr, q3 + multiplier * iqr
        else:
            mean, std = s.mean(), s.std()
            lo, hi = mean - z_threshold * std, mean + z_threshold * std
        X[col] = s.clip(lower=lo, upper=hi)
    return X


# --------------------------------------------------------------------------- #
# Heart Disease
# --------------------------------------------------------------------------- #

HEART_CONTINUOUS = ["age", "trestbps", "chol", "thalach", "oldpeak"]


def preprocess_heart(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Separa features e target do heart.csv (já numérico e sem missings).

    'target': 1 = doença presente, 0 = ausente.
    """
    X = df.drop(columns=["target"]).astype(float)
    y = df["target"].astype(int)
    return X, y


# --------------------------------------------------------------------------- #
# Diabetes 130-US Hospitals
# --------------------------------------------------------------------------- #

# Colunas com proporção elevada de '?' que serão descartadas
DIABETIC_DROP_COLUMNS = [
    "encounter_id",  # identificador
    "patient_nbr",  # identificador
    "weight",  # ~97% ausente
    "payer_code",  # ~52% ausente
    "medical_specialty",  # ~49% ausente
]

# Medicações com valores No/Steady/Up/Down
DIABETIC_MED_COLUMNS = [
    "metformin", "repaglinide", "nateglinide", "chlorpropamide", "glimepiride",
    "acetohexamide", "glipizide", "glyburide", "tolbutamide", "pioglitazone",
    "rosiglitazone", "acarbose", "miglitol", "troglitazone", "tolazamide",
    "examide", "citoglipton", "insulin", "glyburide-metformin",
    "glipizide-metformin", "glimepiride-pioglitazone", "metformin-rosiglitazone",
    "metformin-pioglitazone",
]

MED_ORDINAL = {"No": 0, "Down": 1, "Steady": 2, "Up": 3}

GLU_RESULT = {"None": 0, "Norm": 1, ">200": 2, ">300": 3}
A1C_RESULT = {"None": 0, "Norm": 1, ">7": 2, ">8": 3}

# Colunas numéricas contínuas candidatas a tratamento de outliers
DIABETIC_CONTINUOUS = [
    "time_in_hospital", "num_lab_procedures", "num_procedures",
    "num_medications", "number_outpatient", "number_emergency",
    "number_inpatient", "number_diagnoses",
]


def _parse_age(age: str) -> int:
    """Converte '[60-70)' no limite inferior (60), '?' em -1."""
    if age == "?":
        return -1
    return int(age.replace("[", "").replace(")", "").split("-")[0])


def _icd9_category(code: str) -> str:
    """Agrupa códigos ICD-9 em categorias clínicas amplas."""
    if code in ("?", "", None):
        return "Unknown"
    try:
        num = float(str(code).strip())
    except ValueError:
        num = None
    if num is None:
        return "Unknown"
    if num == 250:
        return "Diabetes"
    if 390 <= num <= 459 or num == 785:
        return "Circulatory"
    if 460 <= num <= 519:
        return "Respiratory"
    if 580 <= num <= 629:
        return "Genitourinary"
    if 140 <= num <= 239:
        return "Neoplasms"
    if 320 <= num <= 389:
        return "Nervous"
    if 1 <= num <= 139:
        return "Infectious"
    if 240 <= num <= 279:
        return "Endocrine"
    if 710 <= num <= 739:
        return "Musculoskeletal"
    return "Other"


ADMISSION_TYPE_GROUP = {
    "Emergency": "Emergency", "Urgent": "Urgent", "Elective": "Elective",
    "Newborn": "Other", "Trauma Center": "Emergency", "Not Available": "Other",
    "NULL": "Other", "Not Mapped": "Other",
}


def _group_by_dict(value, mapping: dict[str, str]) -> str:
    return mapping.get(str(value).strip(), "Other")


def _fill_numeric(df: pd.DataFrame, col: str, fill: int = 0) -> pd.DataFrame:
    """Substitui '?' por um valor numérico (0) e converte para int."""
    df[col] = df[col].replace("?", fill).astype(int)
    return df


class PreprocessDiabetic:
    """Transforma o diabetic_data.csv em features numéricas + target.

    Usa o IDS_mapping.csv para enriquecer semanticamente os IDs de admissão,
    alta e origem, reduzindo-os a categorias compactas (avoid um encoding entre
    índices numéricos arbitrários sem significado).

    Parâmetros:
        binary_target: True -> y = 1 se readmitted == "<30", senão 0.
                       False -> y multiclasse {0: "NO", 1: "<30", 2: ">30"}.
    """

    def __init__(self, binary_target: bool = True):
        self.binary_target = binary_target
        self.diagnosis_categories_: list[str] = []
        self.feature_names_: list[str] = []

    def _category_columns(self, categories: list[str]) -> dict[str, str]:
        return {f"{c}_cat": c for c in categories}

    def transform(self, df: pd.DataFrame, ids_mapping: dict[str, dict[str, str]] | None = None) -> tuple[pd.DataFrame, pd.Series]:
        df = df.copy()
        if ids_mapping is None:
            ids_mapping = {}

        # 1) Remoção de identificadores e colunas com alto missing
        df = df.drop(columns=[c for c in DIABETIC_DROP_COLUMNS if c in df.columns])

        # 2) Tipos de admissão / descarga / origem via IDS_mapping
        for col, group in (
            ("admission_type_id", ADMISSION_TYPE_GROUP),
            ("discharge_disposition_id", "discharge"),
            ("admission_source_id", "source"),
        ):
            if col in df.columns:
                if group == "discharge" or group == "source":
                    valores = ids_mapping.get(
                        col if col == "admission_type_id" else
                        ("discharge_disposition_id" if group == "discharge" else "admission_source_id"),
                        {},
                    )
                    df[f"{col}_grp"] = df[col].map(lambda v: _group_by_dict(v, valores))
                else:
                    df[f"{col}_grp"] = df[col].map(lambda v: _group_by_dict(v, group))
                df[f"{col}_grp"] = df[f"{col}_grp"].fillna("Other")

        # 3) Categóricas textuais
        df["race"] = df["race"].replace("?", "Unknown")
        df["gender"] = df["gender"].map({"Male": 1, "Female": 0}).fillna(0).astype(int)
        df["age_num"] = df["age"].map(_parse_age)

        # 4) Diagnósticos -> categoria ICD-9 do diag_1
        df["diag_cat"] = df["diag_1"].map(_icd9_category)

        # 5) Resultados de laboratório ordinais
        df["max_glu_serum_num"] = df["max_glu_serum"].map(GLU_RESULT).fillna(0).astype(int)
        df["A1Cresult_num"] = df["A1Cresult"].map(A1C_RESULT).fillna(0).astype(int)

        # 6) Medicações ordinais
        for col in DIABETIC_MED_COLUMNS:
            if col in df.columns:
                df[f"{col}_ord"] = df[col].map(MED_ORDINAL).fillna(0).astype(int)

        # 7) Troca de medicação e diabetesMed (binários)
        if "change" in df.columns:
            df["change_bin"] = (df["change"] == "Ch").astype(int)
        if "diabetesMed" in df.columns:
            df["diabetesMed_bin"] = (df["diabetesMed"] == "Yes").astype(int)

        # 8) Numéricas contínuas: corrige '?'
        for col in DIABETIC_CONTINUOUS:
            if col in df.columns:
                df = _fill_numeric(df, col)

        # 9) One-hot das colunas categóricas (antes de remover as originais)
        cat_cols = [c for c in df.columns if c.endswith("_grp")] + ["diag_cat", "race"]
        for col in cat_cols:
            dummies = pd.get_dummies(df[col], prefix=col, dtype=int)
            df = pd.concat([df, dummies], axis=1)
        df = df.drop(columns=cat_cols)

        # 10) Target (antes de remover a coluna readmitted)
        if "readmitted" not in df.columns:
            raise ValueError("Coluna 'readmitted' ausente no dataset.")
        if self.binary_target:
            y = (df["readmitted"] == "<30").astype(int)
        else:
            y = df["readmitted"].map({"NO": 0, "<30": 1, ">30": 2}).astype(int)

        # 11) Remoção das colunas originais já transformadas (inclui readmitted)
        drop_orig = [
            "race", "gender", "age", "admission_type_id", "discharge_disposition_id",
            "admission_source_id", "diag_1", "diag_2", "diag_3", "max_glu_serum",
            "A1Cresult", "change", "diabetesMed", "readmitted",
        ] + DIABETIC_MED_COLUMNS
        df = df.drop(columns=[c for c in drop_orig if c in df.columns])

        # 12) Colunas categóricas originais de texto removidas: cita as grp
        self.feature_names_ = list(df.columns)
        return df.astype(float), y