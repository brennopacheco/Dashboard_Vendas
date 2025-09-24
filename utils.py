from dataset import df
import pandas as pd

def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1_000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1_000
    return f'{prefix} {value:.2f} milhões'


# 1 - Dataframe Receita por Estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()

df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']] \
    .merge(df_rec_estado, left_on='Local da compra', right_index=True) \
    .sort_values('Preço', ascending=False)


# print(df_rec_estado)

# 2 - Receita Mensal
df_rec_mensal = df.set_index('Data da Compra') \
    .groupby(pd.Grouper(freq='M'))[['Preço']].sum() \
    .reset_index()

df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year # Coletando o ano da coluna data
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name() # Coletando o mês da coluna data
print(df_rec_mensal)