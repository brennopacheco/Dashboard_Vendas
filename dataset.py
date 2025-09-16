# Vai ser nossa aplicacao no Streamlit

import json
import pandas as pd

file = open('dados/vendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

print(df)

file.close()