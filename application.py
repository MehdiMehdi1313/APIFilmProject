from flask import Flask, render_template
import http.client
import json
import datetime

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
    'X-RapidAPI-Key': "36399bca7cmsh8058661afeea291p176ed4jsnf349415e3b42",
    'X-RapidAPI-Host': "imdb8.p.rapidapi.com"
    }

# Obtenir la liste des id des acteurs nés aujourd'hui :
def actors(strReq) :

    x = requete(strReq)
    print(x)
    print('\n')

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
    dict_detail = {}
    liste_titre = []

    for id in json_title :
        detail,titre = detail_movie("/title/get-details?tconst="+str(id))
        dict_detail[id] = detail
        liste_titre.append(titre)
    return dict_detail,liste_titre

def detail_movie(strReq) :

    list_movie = []
    movie = requete(strReq)
    titre = movie['title']
    typetitre = movie['titleType']
    year = movie['year']
    url = movie['image']['url']
    list_movie = [titre,typetitre,year,url]
    
    return list_movie,titre

x = datetime.datetime.now()

day = x.strftime("%d")
month = x.strftime("%m")

dict_name, id = actors("/actors/list-born-today?month={0}&day={1}".format(month,day))

award = awards("/actors/get-awards-summary?nconst=" + str(id))

url_image = photo("/actors/get-bio?nconst=" + str(id))

dict_detail,liste_titre = title("/title/get-most-popular-movies?homeCountry=US&purchaseCountry=US&currentCountry=US")

#titre,typetitre,year,url = detail_movie("/title/get-details?tconst=tt0944947")

print(id + '\n')

print(award + '\n')

print(url_image + '\n')

print(dict_detail)

print(liste_titre)




