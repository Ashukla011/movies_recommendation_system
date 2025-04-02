from flask import Flask, jsonify, request
import json

app = Flask(__name__)


with open("./movies.json", "r", encoding="utf-8") as file:
    movie_data = json.load(file)

   

@app.route("/movies", methods=["GET"])
def get_movies():
   
    return jsonify(movie_data)

@app.route("/recommend", methods=["GET"])
def recommend():
    
    movie_name = request.args.get("title")

    
    movie = next((m for m in movie_data["movies"] if m["title"] == movie_name), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    
    similar_movies = [
        m for m in movie_data["movies"]
        if movie["title"] != m["title"]
        and (set(movie["genres"]) & set(m["genres"]) or set(movie["cast"]) & set(m["cast"]))
    ]

    return jsonify({"recommendations": similar_movies})

if __name__ == "__main__":
    app.run(debug=True)
