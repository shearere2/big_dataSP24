import pandas as pd

def combine_dfs(df1:pd.DataFrame, df2:pd.DataFrame) -> pd.DataFrame:
    """Combines the NPI and Grant dataframe

    Args:
        df1 (pd.DataFrame): First dataframe
        df2 (pd.DataFrame): Second dataframe

    Returns:
        pd.DataFrame: Dataframe with Npi and grant data
    """

    df = pd.concat([df1, df2], ignore_index=True)

    return df