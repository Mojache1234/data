# Upload ahca

import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv("ahca_polls.csv", encoding="latin1")
engine = create_engine("mysql+pymysql://tvrtl3b0y:I Am TurtleBoy@localhost/fivethirtyeight")
data.to_sql("ahca_polls", engine, if_exists="replace")

print('Success!')
