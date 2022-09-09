from flask import Flask, render_template
import http.client
import json

app = Flask(__name__)

@app.route("/")
def movie():
    return "<p>Movies list</p>"

def requete(strReq) :
    conn.request("GET", strReq, headers=headers)
    res = conn.getresponse()
    data = res.read()
    list_data = data.decode("utf-8")
    json_data = json.loads(list_data)
    return json_data


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "2291b34504msh32e737e169ea76ap1def00jsn4ee3554760e2",
    'X-RapidAPI-Host': "imdb8.p.rapidapi.com"
    }

# Obtenir la liste des id des acteurs nés aujourd'hui :
def actors(strReq) :

    x = requete(strReq)

    dict_name = {}

    # Obtenir nom prénom des acteurs à partir de leur id et les placer dans un dict :
    for id in x[:1] :

        id = id.split('/')[-2]

        json_bio = requete("/actors/get-bio?nconst=" + str(id))
        name = json_bio['name']
        dict_name[id] = name

    #print(dict_name)

    id = x[3].split('/')[-2] # Pour ne garder que la partie où on a l'id.

    #print('id = ' +str(id) + '\n')

    return dict_name, id

# Obtenir award, détail d'un acteur, image à partir de son id (et afficher son nom, prénom)

def awards(strReq) :

    json_awards = requete(strReq)

    #name = json_bio['name']
    try:
        award = json_awards['awardsSummary']['highlighted']['awardName']
        
    except KeyError:
        award = "Pas d'award"

    print('\n')
    return award

# Photo acteur :

def photo(strReq) : 
    json_detail = requete(strReq)
    url_image = json_detail['image']['url']
    return url_image

# Films les plus populaires :

def title(strReq) :

    json_title = requete(strReq)
    json_title = json_title[:5]
    json_title = list(map(lambda x : x.split('/')[-2] , json_title))
    return json_title


dict_name, id = actors("/actors/list-born-today?month=7&day=27")

award = awards("/actors/get-awards-summary?nconst=" + str(id))

url_image = photo("/actors/get-bio?nconst=" + str(id))

json_title = title("/title/get-most-popular-movies?homeCountry=US&purchaseCountry=US&currentCountry=US")

print(id + '\n')

print(award + '\n')

print(url_image + '\n')

print(json_title)

