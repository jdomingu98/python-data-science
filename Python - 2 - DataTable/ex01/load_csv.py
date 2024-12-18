import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Loads a CSV file into a pandas DataFrame.

    Parameters:
        path: The file path to the CSV file to be loaded.

    Returns:
        A pandas DataFrame with data from file if it is successfully loaded.
        None if there is an error during loading or if the file is not a CSV.

    Raises:
        AssertionError
            - If the file is not a CSV (based on the file extension).
            - If the dataset cannot be loaded successfully.
    """
    try:
        assert path.lower().endswith((".csv")), "File must be a CSV file"
        ds = pd.read_csv(path)
        assert ds is not None, "Cannot load dataset"
        print(f"Loading dataset of dimensions {ds.shape}")
        return ds
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        return None
