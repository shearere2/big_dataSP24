import pandas as pd
import numpy as np


class GrantsData:

    def __init__(self, path: str):
        self.df = pd.read_csv(path, compression='zip')

    def read(self) -> pd.DataFrame:
        """Returns a cleaned dataframe"""
        df = self._select_columns(self.df)
        df = self._clean(df)
        # Data can have NaNs
        # Different types (reasonable)
        # Different types (unreasonable)
        return df

    @staticmethod
    def _select_columns(df: pd.DataFrame) -> pd.DataFrame:
        """Rename and select columns
        NOTE: Underscored methods are "private methods", otherwise 
        meaning that we should only call them from WITHIN the class.

        Args:
            df (pd.DataFrame): dataframe

        Returns:
            pd.DataFrame: the subset, clean name dataframe
        """
        mapper = {
            'APPLICATION_ID': 'grant_application_id',
            'BUDGET_START': 'grant_budget_start',
            'ACTIVITY': 'grant_type',
            'TOTAL_COST': 'grant_total_cost',
            'PI_NAMEs': 'grant_pi_names',
            'PI_IDS': 'grant_pi_ids',
            'ORG_NAME': 'grant_organization',
            'ORG_CITY': 'grant_city',
            'ORG_STATE': 'grant_state',
            'ORG_COUNTRY': 'grant_country'
        }
        return df.rename(columns=mapper)[mapper.values()]
    
    @staticmethod
    def _clean(df: pd.DataFrame) -> pd.DataFrame:
        """Remove NaNs and other cleaning functions

        Args:
            df (pd.DataFrame): dataframe with subset column names

        Returns:
            pd.DataFrame: dataframe free of NaNs
        """
        df['grant_pi_names'] = df['grant_pi_names'].str.split(';')
        df = df.explode('grant_pi_names')
        df['grant_is_contact'] = df['grant_pi_names'].str.lower().str.contains('(contact)')
        df['grant_pi_names'] = df['grant_pi_names'].str.replace('(contact)', '')
        df['grant_both_names'] = df['grant_pi_names'].apply(lambda x: x.split(',')[:2])
        df[['grant_last_name', 'grant_forename']] = pd.DataFrame(df['grant_both_names'].to_list(), index=df.index)
        return df

        



def read_grants_year(year: int | str) -> pd.DataFrame:
    """Read in Grants Data for a year and return as clean dataframe

    Args:
        year (int | str): year to read

    Returns:
        pd.DataFrame: clean dataframe of grants data
    """
    # We know the filename is: RePORTER_PRJ_C_FY2022.zip
    path = 'data/RePORTER_PRJ_C_FY{year}.zip'
    gd = GrantsData(path.format(year=year)) # What does this line do in (year = year)
    return gd.read()


if __name__ == '__main__':

    read_grants_year(2022)
    # Decided to not remove NaNs from the budget start, as I feel date
    # will not be important for my analysis
