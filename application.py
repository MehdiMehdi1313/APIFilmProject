
from flask import Flask, render_template
import requests


app = Flask(__name__)

headers = {
	"X-RapidAPI-Key": "61cd6e2771msh4978653e06ce39dp17ee4djsn76e9c46c6504",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

#get details movies

filmId = {"tconst":"tt10731256"}
urlDetailFilm = "https://imdb8.p.rapidapi.com/title/get-details"

responseFilm = requests.request("GET", urlDetailFilm, headers=headers, params=filmId)

print(responseFilm.text)


def top_movies_id():
    # GET A TOP FIVE MOVIE LIST TITLE ID'S
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {
        "homeCountry": "US",
        "purchaseCountry": "US",
        "currentCountry": "US"
        }

    headers = {
        'x-rapidapi-key': '61cd6e2771msh4978653e06ce39dp17ee4djsn76e9c46c6504',
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=querystring
        )

    reply = response.json()
    top_five_list = "<ul>"

    count = 0
    for title_id in reply:
        if count < 5:
            top_five_list=top_five_list+"<li>"+(title_id[7:-1])+"</li>"
            count += 1

    top_five_list+="</ul>"
    return top_five_list


@app.route("/")
def movie():
    return render_template('index.html',list_film= top_movies_id())