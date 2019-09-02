import sys
import json
import pandas as pd
import numpy as np
import re
import sklearn.metrics.pairwise as pw
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances


# Cliente hizo compra en:
# store_name = 'Adidas kids'
store_name = sys.argv[1]
# Para el primer caso de ALMUERZO + HELADO + CINE colocar store_name='Don Jediondo'.

# Para el segundo caso de MODA_DAMA + CAFE colocar store_name='Zara'.

# Para el tercer caso de MODA_INFANTIL + HELADO colocar store_name='Adidas kids'

# Cargamos la data del historial de compras que est· alojado en el archivo llamado purchase.csv.
df = pd.read_csv(('./data.csv'), sep=';')
df.head()

# Item based recommender system


def item_based_recom(input_dataframe, input_store_name):
    pivot_item_based = pd.pivot_table(input_dataframe,
                                      index='title',
                                      columns=['userId'], values='rating')
    sparse_pivot = sparse.csr_matrix(pivot_item_based.fillna(0))
    recommender = pw.cosine_similarity(sparse_pivot)
    recommender_df = pd.DataFrame(recommender,
                                  columns=pivot_item_based.index,
                                  index=pivot_item_based.index)
    # Item Rating Based Cosine Similarity
    cosine_df = pd.DataFrame(
        recommender_df[store_name].sort_values(ascending=False))
    cosine_df.reset_index(level=0, inplace=True)
    cosine_df.columns = ['title', 'cosine_sim']
    return cosine_df
# FunciÛn que toma el historial(df), la tienda en la que acaba de comprar y devuelve un top de los dos resultados m·s cercanos.


def generate_recomendations(df, store_name, top_results=2):
    # print("Stores you might enjoy based that you made a purchase in:", store_name)
    # Item Rating Based Cosine Similarity
    cos_sim = item_based_recom(df, store_name)
    # display(cos_sim[1:top_results+1])
    return cos_sim[1:top_results+1]


# Veamos las 2 recomendaciones que escogemos de acuerdo a lo que compramos:
# generate_recomendations(df,store_name,2)
# generate_recomendations(df,store_name,2).to_json(r'C:/Users/jfosorio/Documents/recomendados.json')
print(json.dumps(generate_recomendations(df, store_name, 2).to_dict('dict')))
# print(generate_recomendations(df,store_name,2))


# import sys
# import json

# hola = sys.argv[1]

# print(json.dumps(dict({"a": 1, "b": 2})))
