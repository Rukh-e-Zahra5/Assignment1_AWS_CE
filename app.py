from flask import Flask
import requests

app = Flask(__name__)

API_URL = "https://api.tvmaze.com/search/shows?q=event"

@app.route("/")
def home():
    response = requests.get(API_URL)
    data = response.json()

    events = []
    for item in data[:10]:
        show = item["show"]

        venue = "Online"
        if show.get("network"):
            venue = show["network"]["name"]

        events.append({
            "title": show["name"],
            "date": show.get("premiered", "Unknown"),
            "venue": venue,
            "description": show.get("summary", "No description")
        })

    return {"events": events}

if __name__ == "__main__":
    app.run(debug=True)