import pandas as pd 
import sqlite3
import numpy as np

con = sqlite3.connect("oscar.db")
cur = con.cursor()

query = """
SELECT * FROM films
JOIN ratings ON films.Id = film_id;
"""

cur.execute(query)

films = []
for i, data in enumerate(cur):
    films.append(list(data))

for item in films:
    item.pop()

cur.close()
con.close()

df = pd.DataFrame(films)
print(df)
resultado = df[0].drop_duplicates()
resultado.reset_index(drop=True, inplace=True)
print(resultado)

# Média (ponderada)
weighted_average = lambda group: (group[3] * group[2]).sum() / group[3].sum()
resultado = df.groupby(1).apply(weighted_average, include_groups=False)
print(resultado)

# Desvio Padrão

def weighted_variance(values, weights):
    average = (values * weights).sum() / weights.sum()
    variance = ((values - average)**2 * weights).sum() / weights.sum()
    return variance

weighted_std = lambda values, weights: weighted_variance(values, weights)**0.5
desvio_padrao_ponderado = weighted_std = weighted_std(df[2], df[3])
print(desvio_padrao_ponderado) #ta errado ainda calma :( 
# Lei da Sucessão de Laplace




