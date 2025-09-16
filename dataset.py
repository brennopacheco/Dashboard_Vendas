# Vai ser nossa aplicacao no Streamlit

import json
import pandas as pd

file = open('dados/vendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d%m%Y') # alterando o tipo de dado

# print(df['Data da Compra'])

file.close()