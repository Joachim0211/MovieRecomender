import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity


st.title("Movie Recommendation")
 
st.write("""
### Project description
This is a protptype where users can see the top rated movies and movies that we recommend based on similarity of a movie that you search. 
 
""")



link = '[Evaluation](https://www.google.de/?hl=de)'


if st.button('Go to Model Evaluation'):
     st.markdown(link, unsafe_allow_html=True)
else:
     st.write('No such Website')

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
#tags = pd.read_csv('tags.csv')

with st.expander("See the best movie ever"):
    st.write("""
         The Movie below is the favourite 
         movie of most celebrities
     """)
    st.image("https://berlin.museum-digital.de/singleimage.php?imagenr=1850")
    
name_list = movies['title'].tolist()
m_name = st.selectbox('Please enter the name of a movie', name_list)
n1 = st.text_input('Please enter the number of top rated movies that you would like to see') 
if n1=="":
    n1="1"

#def hit_movies(n):
#    movie_ratings = movies.merge(ratings, on = 'movieId', how = 'left')
#    sorted_movies = pd.DataFrame(movie_ratings.groupby('movieId').rating.mean().sort_values(ascending = False))
#    sorted_movies['number_of_ratings']=ratings.groupby('movieId').userId.count()
#    sorted_movies['rating_value'] = sorted_movies['rating'] * sorted_movies['number_of_ratings']
#    top_list = pd.DataFrame(sorted_movies['rating_value'].sort_values(ascending = False).reset_index())
#    top_movies = []
#    for movieId in top_list['movieId']:
#        top_movies.append(movies.loc[movies['movieId'] == movieId, 'title'].items())
#    top_movies = pd.DataFrame(top_movies)
#    return top_movies.head(n)
#hit_movies(int(n))

name1 = movies.loc[movies['title']==m_name, 'movieId'].item()

def sim_movies(name, n):
    rating_crosstab = pd.pivot_table(data=ratings, values='rating', index='userId', columns='movieId')
    m_ID = name
    m_ratings = rating_crosstab[m_ID]
    m_ratings = m_ratings[m_ratings>=0] # exclude NaNs
    similar_to_m_ID = rating_crosstab.corrwith(m_ratings)
    corr_m_ID = pd.DataFrame(similar_to_m_ID, columns=['PearsonR'])
    corr_m_ID.dropna(inplace=True)
    rating2 = pd.DataFrame(ratings.groupby('movieId')['rating'].mean())
    rating2['rating_count'] = ratings.groupby('movieId')['rating'].count()
    movie_corr_summary = corr_m_ID.join(rating2['rating_count'])
    movie_corr_summary.drop(m_ID, inplace=True) # drop the selected movie
    topn = movie_corr_summary[movie_corr_summary['rating_count']>=10].sort_values('PearsonR', ascending=False).head(n)
    m_name = movies[['movieId', 'title', 'genres']]
    topn = topn.merge(m_name, left_index=True, right_on="movieId")
    st.write(topn[['title', 'genres', 'rating_count']])

st.write('Movies you might like')
sim_movies(name1, int(n1))

n3 = st.text_input('Whats hot at the moment - put in a number')
if n3=="":
    n3="1"
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
        # top_movie_list.append(b['movieId'].temp)
    return top_movie_list

recom_movies(n3)
