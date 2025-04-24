from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template
import wikipedia
import random

app = Flask(__name__)
favorite_articles = []
languages = {
    "en": "English",
    "ko": "Korean",
    "hi": "Hindi",
    "ar": "Arabic"
}


@app.route("/search", methods=["POST"])
def search():
    data = request.json
    query = data.get("query", "")
    try:
        page = wikipedia.page(query)
        return jsonify({
            "title": page.title,
            "summary": page.summary,
            "url": page.url
        })
    except wikipedia.exceptions.PageError:
        return jsonify({"error": "Page not found."}), 404
    except wikipedia.exceptions.DisambiguationError as e:
        return jsonify({"error": "Disambiguation error", "options": e.options}), 400


@app.route("/random", methods=["GET"])
def random_page():
    try:
        title = wikipedia.random()
        page = wikipedia.page(title)
        return jsonify({
            "title": page.title,
            "summary": page.summary,
            "url": page.url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/favorites", methods=["POST"])
def add_favorite():
    data = request.json
    article = data.get("article")
    favorite_articles.append(article)
    return jsonify({"message": f"{article} added to favorites"})


@app.route("/favorites", methods=["GET"])
def view_favorites():
    return jsonify({"favorites": favorite_articles})


@app.route("/language", methods=["POST"])
def set_language():
    data = request.json
    lang_code = data.get("code")
    if lang_code in languages:
        wikipedia.set_lang(lang_code)
        return jsonify({"message": f"Language set to {languages[lang_code]}."})
    else:
        return jsonify({"error": "Invalid language code."}), 400

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
