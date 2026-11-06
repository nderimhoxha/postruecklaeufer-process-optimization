import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

password = os.environ["MYSQL_PASSWORD"]
url = URL.create("mysql+pymysql", username="root", password=password,
                 host="localhost", database="postrueckl")
engine = create_engine(url)

cases = pd.read_csv("data/cases.csv")
cases.to_sql("cases", engine, if_exists="append", index=False)