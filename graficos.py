import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra', # para passar o mouse por cima e obter um retorno
    hover_data={'lat': False, 'lon': False},
    title='Receita por Estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mes',
    y='Preço',
    markers=True,
    range_x=(0, df_rec_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)
grafico_rec_mensal.update_layout(yaxis_title='Receita')

grafico_rec_estado = px.bar(
    df_rec_estado.head(),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top Receita por Estado'
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(),
    text_auto=True,
    title='Top 5 Categorias com Maior Receita'

)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values(by='sum', ascending=False).head(5),
    x='sum',
    y=df_vendedores[['sum']].sort_values(by='sum', ascending=False).head().index,
    text_auto=True,
    title='Top Vendedores por Receita'
)