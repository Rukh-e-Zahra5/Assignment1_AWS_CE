from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey=YOUR_API_KEY"

@app.route("/")
def home():
    
    events = []

    try:
        response = requests.get(API_URL)
        data = response.json()

        if "_embedded" in data:
            for event in data["_embedded"]["events"][:5]:
                events.append({
                    "name": event["name"],
                    "date": event["dates"]["start"]["localDate"],
                    "venue": event["_embedded"]["venues"][0]["name"]
                })
    except:
        events = []

    return render_template("index.html", events=events)


if __name__ == "__main__":
    app.run(debug=True)