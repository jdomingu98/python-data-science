import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    if not path.lower().endswith((".csv")):
        return None
    ds = pd.read_csv(path)
    if ds is not None:
        print(f"Loading dataset of dimensions {ds.shape}")
    return ds
