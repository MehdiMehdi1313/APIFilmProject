from flask import Flask, render_template, request, redirect, url_for
import requests
import http.client
import json

app = Flask(__name__)

@app.route("/")
def movie():
    return render_template('index.html', dictActors=displayActorsName())

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")


headers = {
        "X-RapidAPI-Key": "2291b34504msh32e737e169ea76ap1def00jsn4ee3554760e2",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

def requete(strReq) :
    conn.request("GET", strReq, headers=headers)
    res = conn.getresponse()
    data = res.read()
    list_data = data.decode("utf-8")
    json_data = json.loads(list_data)
    return json_data

# Fonction qui fourni en sortie le nom de chaque acteur né aujourd'hui
def displayActorsName():
    
    #  Obtenir la liste des id des acteurs nés aujourd'hui :
    x = requete("/actors/list-born-today?month=7&day=27")

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
def awards(id) :
    json_awards = requete("/actors/get-awards-summary?nconst="+str(id))

    try:
        award = json_awards['awardsSummary']['highlighted']['awardName']
        
    except KeyError:
        award = "Pas d'award"

    return "<h2>Les awards de l'acteur :</h2><p>- "+award+"</p>"









