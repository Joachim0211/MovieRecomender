import streamlit as st
import pandas as pd
import pickle
import sklearn

st.title("Favourite Movies")
#st.write()
a=st.text_input("Do you want to see the most popular movies of all times")
b=st.text_input("Do you want to see your favorite movies")

dflinks = pd.read_csv('links.csv')
dfmovies = pd.read_csv('movies.csv')
dfratings = pd.read_csv('ratings.csv')
#dftags = pd.read_csv('tags.csv')
# a=pd.DataFrame(dfratings.groupby('movieId')['rating'].mean())
# b = merge(a, dfmovies, how='left', on=['movieId'])


top_movie_list = []
def recom_movies(n):
    rating = pd.DataFrame(dfratings.groupby('movieId')['rating'].mean())
    rating['movieId'] = rating.index
    rating['rating_count'] = dfratings.groupby('movieId')['rating'].count()
    rating['hrating'] = rating['rating'] * (rating['rating_count']/100)
    rated = rating.sort_values(by='hrating', ascending=False)
    for i in range(n):
        temp = rated.iloc[i]['movieId']
        print(temp)
        dfmovies.loc[dfmovies['movieId'] == temp, 'title']
        top_movie_list.append(dfmovies.loc[dfmovies['movieId'] == temp, 'title'].item()) 
    return top_movie_list

recom_movies(int(a))  


