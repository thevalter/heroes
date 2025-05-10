import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search_hero():
    query = request.args.get('hero')
    results = []

    if query:
        url = f"https://superheroapi.com/api/{api_key}/search/{query}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            print(data)

    return render_template('search.html', results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
