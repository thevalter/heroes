
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search_hero():
    query = request.args.get('hero')
    results = []

    if query:
        api_key = "a929600f115180e1e7e9e2dd073c857b"
        url = f"https://superheroapi.com/api/{api_key}/search/{query}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            print(data)
            
    return render_template('search.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)