from flask import Flask, render_template, request
import http.client
import json
import datetime

app = Flask(__name__)


@app.route("/")
def movie():
    return render_template('index.html', dictActors=displayActorsName(), listFilm=title())


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")


headers = {
    "X-RapidAPI-Key": "71d08ccdbdmshdb55338d4859e1fp196e2ajsnab61f3412cd3",
    "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

# Méthode qui exécute une requête HTTP


def requete(strReq):
    conn.request("GET", strReq, headers=headers)
    res = conn.getresponse()
    data = res.read()
    list_data = data.decode("utf-8")
    json_data = json.loads(list_data)
    return json_data

# Fonction qui fournit en sortie le nom de chaque acteur né aujourd'hui


def displayActorsName():
    date = datetime.datetime.now()
    day = date.strftime("%d")
    month = date.strftime("%m")

    #  Obtenir la liste des id des acteurs nés aujourd'hui :
    x = requete("/actors/list-born-today?month={0}&day={1}".format(month, day))

    dict_name = {}

    # Obtenir nom prénom des acteurs à partir de leur id :
    for id in x[:10]:

        id = id.split('/')[-2]
        json_bio = requete("/actors/get-bio?nconst=" + str(id))
        name = json_bio['name']
        dict_name[id] = name

    id = x[3].split('/')[-2]
    return dict_name

# Obtenir award, détail d'un acteur, image à partir de son id (et afficher son nom, prénom)


@app.route("/<id>")
def detailsActor(id):
    award = awards(id)
    url_image = photo(id)

    contentToDisplay = "<h2>Les awards de l'acteur :</h2><li>"+award+"</li>" + \
        "<h2>Sa photo :</h2>"+"<img src='"+url_image + \
        "' height='720' width='720' alt='image auteur'/>"

    return contentToDisplay

# Méthode qui fournit les récompenses obtenues par un acteur grâce à son id


def awards(id):
    json_awards = requete("/actors/get-awards-summary?nconst="+str(id))

    try:
        award = json_awards['awardsSummary']['highlighted']['awardName']

    except KeyError:
        award = "Pas d'award attribué"

    return award

# Obtenir photo d'un acteur à partir de son id


def photo(id):
    json_detail = requete("/actors/get-bio?nconst=" + str(id))
    url_image = json_detail['image']['url']

    return url_image

# Fournit les id de films populaires et leur titre associé


def title():

    json_title = requete(
        "/title/get-most-popular-movies?homeCountry=US&purchaseCountry=US&currentCountry=US")
    json_title = json_title[:10]
    json_title = list(map(lambda x: x.split('/')[-2], json_title))
    dict_detail = {}

    for id in json_title:
        titre = title_movie("/title/get-details?tconst="+str(id))
        dict_detail[id] = titre

    return dict_detail

# Méthode qui retourne le titre d'un film en fonction de son id


def title_movie(strReq):

    movie = requete(strReq)
    titre = movie['title']

    return titre


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(debug=True)
