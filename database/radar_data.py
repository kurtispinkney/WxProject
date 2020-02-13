from config import config

import pandas as pd
from sqlalchemy import create_engine

connect_params = config()

engine_str = f"postgresql+psycopg2://" \
             f"{connect_params['user']}:" \
             f"{connect_params['password']}" \
             f"@{connect_params['host']}/" \
             f"{connect_params['database']}"

db_engine = create_engine(engine_str)

df = pd.read_csv("../EDA/aws_radar_locations.csv")

df.to_sql("radars", db_engine, if_exists="append", index=False)
