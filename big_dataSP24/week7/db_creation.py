import pandas as pd
import sqlalchemy
from week6 import grants_reader
from week6 import npi_reader


def db():
    engine = sqlalchemy.create_engine('sqlite:///data/grant_npi.db')
    conn = engine.connect()
    return conn

# WE MUST HAVE SAME COLUMNS IN DATAFRAME AND DATABASE!
def npi_csv_to_db(csv_path: str):
    df = npi_reader.read()
    df.to_sql('npi',db(), if_exists='append',index=False)

def grant_csv_to_db(csv_path: str):
    df = grants_reader.read_grants_year(2022)
    df.to_sql('grant',db(), if_exists='append',index=False) # method = 'multi' # chunksize=1000    

if __name__ == "__main__":
    npi_csv_to_db('')
    grant_csv_to_db('')
