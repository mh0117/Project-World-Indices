import pandas as pd
import psycopg2
from sqlalchemy import create_engine
# POSTGRESQL_URL = 'postgresql://postgres:postgres@localhost/mariam'
POSTGRESQL_URL = 'postgres://sowmjntrzdsftr:883ebb9c4b9f387fbc875a06eb1defe4353a6371903b17952f4ce8b1023c9d3a@ec2-54-83-192-245.compute-1.amazonaws.com:5432/dbae2u93isa3ec'
engine = create_engine(POSTGRESQL_URL)

try:
    data = pd.read_sql_query('select * from population_data', engine)
except:
    df = pd.read_csv('public/data/population_data.csv', encoding='latin1')

    years = list(range(1960, 2018))
    new_columns = ['country_name', 'country_code'] + list(range(1960, 2018))
    newdf = df.iloc[:, 2:]
    newdf.columns = new_columns
    newdf.to_sql('population_data', engine, index=False)
