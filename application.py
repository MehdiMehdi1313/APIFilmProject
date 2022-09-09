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

x = requete("/actors/list-born-today?month=7&day=27")

dict_name = {}

# Obtenir nom prénom des acteurs à partir de leur id et les placer dans un dict :
for id in x[:1] :

    id = id.split('/')[-2]

    json_bio = requete("/actors/get-bio?nconst=" + str(id))
    name = json_bio['name']
    dict_name[id] = name

print(dict_name)

id = x[3].split('/')[-2] # Pour ne garder que la partie où on a l'id.

print('id = ' +str(id) + '\n')

# Obtenir award, détail d'un acteur, image à partir de son id (et afficher son nom, prénom)
json_awards = requete("/actors/get-awards-summary?nconst=" + str(id))

#name = json_bio['name']
try:
    print(json_awards['awardsSummary']['highlighted']['awardName'])
    award = json_awards['awardsSummary']['highlighted']['awardName']
    
except KeyError:
    print("Pas d'award")
    award = "Pas d'award"

print('\n')

# Photo acteur :
json_detail = requete("/actors/get-bio?nconst=" + str(id))
url_image = json_detail['image']['url']

print('\n')
print(url_image)