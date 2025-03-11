import pandas as pd
import dict_to_db as d_t_db

def csv_to_dict():
    df = pd.read_csv("Clientes.csv")
    d = df.to_dict(orient='list')
    return d

data = csv_to_dict()

for i in range(30):
    d_t_db.send_data_to_db(i, data)