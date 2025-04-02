import streamlit as st
import requests


API_URL = "http://127.0.0.1:5000"

st.title(" :blue[Movie Recommendation System]")


@st.cache_data
def fetch_movies():
    response = requests.get(f"{API_URL}/movies")
    if response.status_code == 200:
        return response.json().get("movies", [])
    else:
        return []

movies = fetch_movies()


all_genres = set()
for movie in movies:
    all_genres.update(movie.get("genres", []))


st.sidebar.header(" :blue[Search & Filters]",divider="blue")
search_query = st.sidebar.text_input("Search Movie")
selected_genre = st.sidebar.selectbox("Filter by Genre", ["All"] + sorted(all_genres))  


menu = st.selectbox(":blue[Choose an option]", ["Recommend Movies", "Browse All Movies"])


if menu == "Recommend Movies":
    movie_name = st.text_input(":blue[Enter Movie Name]")
    
    if st.button(" Get Recommendations"):
        response = requests.get(f"{API_URL}/recommend?title={movie_name}")
        
        if response.status_code == 200:
            data = response.json()
            
            if "recommendations" in data and data["recommendations"]:
                st.subheader("Recommended Movies:")
                for movie in data["recommendations"]:
                    with st.container():
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.image(movie.get("thumbnail", ""), width=150)
                        with col2:
                            st.markdown(f"### [{movie['title']}]({movie.get('href', '#')}) ({movie.get('year', 'Unknown')})")
                            st.write(movie.get("extract", "No description available."))
                            st.write(" Genres: " + ", ".join(movie.get("genres", [])))
                            st.write("---")
            else:
                st.error(" No recommendations found for this movie.")
        else:
            st.error(" Error fetching recommendations!")

elif menu == "Browse All Movies":
    if not movies:
        st.error(" No movies available! Check if API is running.")
    else:
        st.subheader(":blue[All Movies]")
        for movie in movies:
            if selected_genre == "All" or selected_genre in movie.get("genres", []):
                with st.container():
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(movie.get("thumbnail", ""), width=150)
                    with col2:
                        st.markdown(f"### [{movie['title']}]({movie.get('href', '#')}) ({movie.get('year', 'Unknown')})")
                        st.write(movie.get("extract", "No description available."))
                        st.write(":blue[Genres:] " + ", ".join(movie.get("genres", [])))
                        st.write(":blue[Cast:] " + ", ".join(movie.get("cast", [])))
                        st.write("---")
