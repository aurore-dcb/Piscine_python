import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a dataset from a CSV file \
        and write the dimensions of the dataset."""
    try:
        assert isinstance(path, str), "Path must be a string"
        assert path.endswith('.csv'), "Path must end with .csv"
    except AssertionError as e:
        print(f"Error: {e}")
        return None
    try:
        with open(path, 'r') as file:
            data = pd.read_csv(file, sep=',')
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
