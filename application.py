from flask import Flask, render_template
import requests
import http.client
import json

app = Flask(__name__)

@app.route("/")
def movie():
    return render_template('index.html', listActors=displayActorsName())


# Fonction qui fourni en sortie le nom de chaque acteur né aujourd'hui
def displayActorsName():
    

    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")


    headers = {
        "X-RapidAPI-Key": "f734e1d237mshcbadac401f1ca46p1b2084jsn68dca2e76611",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    #  Obtenir la liste des id des acteurs nés aujourd'hui :
    conn.request("GET", "/actors/list-born-today?month=7&day=27", headers=headers)

    res = conn.getresponse()
    
    data = res.read()

    list_id = data.decode("utf-8")

    x = json.loads(list_id)

    dict_name = {}

    # Obtenir nom prénom des acteurs à partir de leur id :
    for id in x :

        id = id.split('/')[-2]
        conn.request("GET", "/actors/get-bio?nconst=" + str(id), headers=headers)
        res = conn.getresponse()
        data = res.read()
        list_bio = data.decode("utf-8")
        json_bio= json.loads(list_bio)
        name = json_bio['name']
        dict_name[id] = name

    id = x[3].split('/')[-2]
    my_list = list(dict_name.values())
    return my_list


