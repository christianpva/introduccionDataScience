# -*- coding: utf-8 -*-
"""Introducción a Data Science.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OhYqmcuRfPp3GYdTvE_wPgz6QfxaE8IX
"""

import pandas as pd
notas = pd.read_csv("ratings.csv") 
#notas = pd.read_csv("drive/My Drive/Alura/ratings.csv")
notas.head()

notas.shape

notas.columns = ["usuarioId", "peliculaId", "nota", "momento"]
notas.head()

notas['nota']

notas['nota'].unique()

notas['nota'].value_counts()

notas['nota'].mean()

notas.nota.head()

notas.nota.plot()

notas.nota.plot(kind='hist')

print("Promedio",notas['nota'].mean())
print("Mediana",notas['nota'].median())

notas.nota.describe()

import seaborn as sns

sns.boxplot(notas.nota)

"""#Analizando las películas"""

peliculas = pd.read_csv("movies.csv") 
peliculas.head()

"""#Analizando notas de películas específicas"""

peliculas.columns = ["peliculaId", "titulo", "generos"]

notas.query("peliculaId==1")

notas.query("peliculaId==1").nota

notas.query("peliculaId==1").nota.mean()

notas.query("peliculaId==2").nota.mean()

"""# Promedio de las notas de las peliculas"""

notas.groupby("peliculaId").mean()["nota"]

promedios_por_pelicula = notas.groupby("peliculaId").mean().nota
promedios_por_pelicula.head()

promedios_por_pelicula.plot(kind = "hist")

sns.boxplot(promedios_por_pelicula)

promedios_por_pelicula.describe()

sns.distplot(promedios_por_pelicula, bins = 10)

import matplotlib.pyplot as plt
plt.hist(promedios_por_pelicula)
plt.title("Histograma de los promedios de las películas")

sns.boxplot(y=promedios_por_pelicula)

plt.figure(figsize=(5,8))

plt.figure(figsize=(5,8))
sns.boxplot(y=promedios_por_pelicula)

import pandas as pd
tmdb = pd.read_csv("tmdb_5000_movies.csv")
tmdb.head()

tmdb.original_language

tmdb.original_language.unique()

#Categorico ordinal

#primaria 
#secundaria
#universidad

#primaria >> #secundria >> #universidad

#budget --> cuantitaiva continua

#numero de votos  --> cuantitativa de intervalo

#3,5 votos 

#1 2 3 -> 1 


#Notas  0,5 5, 0,5 2,7 --> cuantitiva por intervalo #Notas  0,5 5, 0,5 2,7 --> cuantitiva por intervalo

tmdb.original_language.value_counts()

tmdb.original_language.value_counts().to_frame().reset_index()

contador_idiomas = tmdb.original_language.value_counts().to_frame().reset_index()
contador_idiomas.columns = ["idioma_original","total"]
contador_idiomas.head()

sns.barplot(x="idioma_original",y="total",data = contador_idiomas)

sns.catplot(x="original_language",kind = "count", data = tmdb)

import matplotlib.pyplot as plt

plt.pie(contador_idiomas.total,labels = contador_idiomas.idioma_original)

total_por_idioma = tmdb.original_language.value_counts()
total_general = total_por_idioma.sum()
total_ingles = total_por_idioma.loc["en"]
total_diferencia = total_general - total_ingles
print(total_general,total_ingles, total_diferencia)

datos = {
    'idioma':['ingles','otros'],
    'total' :[total_ingles,total_diferencia]
}

datos

datos = pd.DataFrame(datos)
datos

sns.barplot(x="idioma",y="total",data=datos)

tmdb.query("original_language != 'en'").original_language.value_counts()

peliculas_sin_idioma_ingles = tmdb.query("original_language != 'en'")

sns.catplot(x="original_language", kind = "count", data = peliculas_sin_idioma_ingles)

plt.figure(figsize=(5,16))
sns.catplot(x="original_language", kind = "count", data = peliculas_sin_idioma_ingles)

sns.catplot(x="original_language", kind = "count", 
            data = peliculas_sin_idioma_ingles,
              aspect = 2)

total_idiomas_otras_peliculas = tmdb.query("original_language != 'en'").original_language.value_counts()

sns.catplot(x="original_language", kind = "count", 
            data = peliculas_sin_idioma_ingles,
              aspect = 2,
                order = total_idiomas_otras_peliculas.index)

sns.catplot(x="original_language", kind = "count", 
            data = peliculas_sin_idioma_ingles,
              aspect = 2,
                order = total_idiomas_otras_peliculas.index,
                  palette = "GnBu_d")

"""1) inglés es el más predominante
2) ditribución de los otros idiomas
"""