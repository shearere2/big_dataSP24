import pandas as pd
import sqlalchemy

from big_dataSP24.week6 import grants_reader
from big_dataSP24.week6 import npi_reader


def db():
    engine = sqlalchemy.create_engine('sqlite:///data/grant_npi.db')
    conn = engine.connect()
    return conn


def grants_csv_to_db():
    df = grants_reader.read_grants_year(22)
    df.to_sql('grants',
              db(),
              if_exists='append',
              index=False)
    
def npi_csv_to_db(csv_path: str):
    df = npi_reader.read(csv_path)
    df.to_sql('npi',
              db(),
              if_exists='append',
              index=False)


# # Another slash
# engine = sqlalchemy.create_engine(
#     'sqlite:////Users/arthur/teaching/duq_ds3_2023/data/live_test_sqlite.db')
# df = pd.read_csv('data/affiliations.csv')

# # Have to account for SQLAlchemy v2
# with engine.connect() as conn:
#     df.to_sql('aff', conn, index=False, if_exists='append')
#     df2 = pd.read_sql(sqlalchemy.text('SELECT * FROM aff'), conn)
# print(df2)


if __name__ == '__main__':
    grants_csv_to_db()
    npi_csv_to_db('data/npidata_pfile_20240205-20240211.csv')