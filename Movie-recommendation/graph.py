import json
import networkx as nx
import heapq  

class MovieGraph:
    def __init__(self, json_file):
        self.movie_graph = nx.Graph()
        self.load_data(json_file)

    def load_data(self, json_file):
        """Load movie data from JSON and build the graph"""
        with open(json_file, encoding="utf-8") as file:
            movie_data = json.load(file)

        for movie in movie_data:
            self.movie_graph.add_node(movie["title"], genres=movie["genres"], cast=movie["cast"])

        # Add edges based on genre similarity
        for movie1 in movie_data:
            for movie2 in movie_data:
                if movie1["title"] != movie2["title"]:
                    common_genres = set(movie1["genres"]) & set(movie2["genres"])
                    if common_genres:
                        self.movie_graph.add_edge(
                            movie1["title"], movie2["title"], weight=len(common_genres)
                        )

    def dijkstra(self, start_movie):
        """Find the shortest paths from start_movie to all other movies using Dijkstra's algorithm"""
        distances = {movie: float('inf') for movie in self.movie_graph.nodes}
        distances[start_movie] = 0

        pq = [(0, start_movie)]  # (distance, movie)

        while pq:
            current_distance, current_movie = heapq.heappop(pq)

            if current_distance > distances[current_movie]:
                continue

            for neighbor, attributes in self.movie_graph[current_movie].items():
                weight = attributes['weight']
                distance = current_distance + 1 / weight  

                # If a shorter path is found, update the distance and push to the queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def recommend_movies(self, movie_name, num_recommendations=5):
        """Return a list of recommended movies based on Dijkstra's algorithm"""
        if movie_name not in self.movie_graph:
            return ["Movie not found!"]

        # Run Dijkstra's algorithm to get the shortest paths
        distances = self.dijkstra(movie_name)

        # Sort movies by the shortest distance (best recommendation)
        recommended_movies = sorted(distances.items(), key=lambda x: x[1])

        # Return the top N recommendations (excluding the starting movie)
        return [movie for movie, _ in recommended_movies[1:num_recommendations+1]]


movie_graph = MovieGraph("movies.json")

movie_name = "The Matrix"
recommended_movies = movie_graph.recommend_movies(movie_name, num_recommendations=5)

print(f"Movies recommended based on '{movie_name}':")
for movie in recommended_movies:
    print(movie)
