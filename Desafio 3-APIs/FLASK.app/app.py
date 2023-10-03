from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route("/locations")
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(locations)

    locations = []

    for location in dict["results"]:
        location = {
            "id": location["id"],
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
        }

        locations.append(location)

    return render_template("locations.html", locations=locations)


@app.route("/location/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    characters = []
    
    for char_url in location['residents']:
        char_response = urllib.request.urlopen(char_url)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters.append(char_dict)   
    location['characters']= characters

    return render_template("location.html", location=location)

@app.route("/episodes")
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes = []

    for episode in dict["results"]:
        episode = {
            "id": episode["id"],
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"],
        }

        episodes.append(episode)

    return render_template("episodes.html", episodes=episode)

@app.route("/episodes/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episode = json.loads(data)

    characters = []
    
    for char_url in episode['characters']:
        char_response = urllib.request.urlopen(char_url)
        char_data = char_response.read()
        char_dict = json.loads(char_data)
        characters.append(char_dict)   
    episode['characters']= characters

    return render_template("episode.html", episode=episode)

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)

@app.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict =json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters.append(character)
    return {"characters": characters}
