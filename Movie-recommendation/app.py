import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000"

st.title("🎬 Movie Recommendation System")

menu = st.selectbox("Choose an option", ["Recommend Movies", "Browse All Movies"])

if menu == "Recommend Movies":
    movie_name = st.text_input("Enter Movie Name")
    if st.button("Get Recommendations"):
        response = requests.get(f"{API_URL}/recommend?title={movie_name}")
        data = response.json()

        if "recommendations" in data:
            st.subheader("Recommended Movies:")
            for movie in data["recommendations"]:
                st.image(movie["thumbnail"], width=150)
                st.markdown(f"### [{movie['title']}]({movie['href']}) ({movie['year']})")
                st.write(movie["extract"])
                st.write("---")
        else:
            st.error("Movie not found!")

elif menu == "Browse All Movies":
    response = requests.get(f"{API_URL}/movies")
    data = response.json()
    
    st.subheader("All Movies")
    for movie in data["movies"]:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(movie["thumbnail"], width=150)
            with col2:
                st.markdown(f"### [{movie['title']}]({movie['href']}) ({movie['year']})")
                st.write(movie["extract"])
                st.write("🎭 Genres: " + ", ".join(movie["genres"]))
                st.write("🎬 Cast: " + ", ".join(movie["cast"]))
                st.write("---")
