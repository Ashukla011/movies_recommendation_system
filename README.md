# Movie Recommendation System

 **1. Introduction**
 
The **Movie Recommendation System** is a web application that suggests movies to users based on their preferences. It uses **Dijkstra’s Algorithm** to find the most similar movies based on genres and cast. The system is built using **Django** and **Flask** for the backend, a JSON file for storing movie data, and a Python Streamlit / PyQt / Tkinter for the frontend.

 ### some basic command are
 first colne the project to run in local system 
 
1. cd movie-recommendation
2. run the json file server <code> python server.py</code>
3. install <code>pip install streamlit </code>
4. run the using command <code>streamlit run app.py </code>




**2. Technology Stack**

| Technology  | Purpose  |
|-------------|----------|
| **Django** | Main backend framework for handling web requests |
| **Flask** | Used for microservices and API integration |
| **Python** | Programming language for the logic and algorithms |
| **JSON** | Stores movie data (title, genres, cast, ratings) |
| **NetworkX** | NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. |
| **Streamlit** | simple web-based UI that runs in a browser and is easy to deploy. |

---

**3. Algorithm Used: Dijkstra’s Algorithm**

- The **Movie Graph** is built using **NetworkX**.
- Each movie is treated as a **node**, and edges are created between similar movies.
- **Edge weights** represent similarity based on shared genres and cast members.
- **Dijkstra’s Algorithm** is used to find the shortest path between a selected movie and similar movies.
- The movies with the lowest distance (highest similarity) are recommended.

**Steps of the Algorithm:**
1. Load movie data from a **JSON file**.
2. Create a **graph** where each movie is a **node**.
3. Connect movies based on **common genres and cast**.
4. Apply **Dijkstra’s Algorithm** to find the most similar movies.
5. Return the top **recommended movies**.

---

**4. Features**
- **Home Page:** Displays popular and trending movies.
- **Movie Search:** Users can search for movies by title or genre.
- **Recommendations:** Suggests movies similar to a selected movie.
- **Movie Details Page:** Shows movie information (cast, genre, rating, etc.).

---

**5. Conclusion**
This system efficiently recommends movies using **graph-based algorithms** and the combination of **Django, Flask, JSON**, 



