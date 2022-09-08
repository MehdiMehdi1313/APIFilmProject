from flask import Flask, render_template
import http.client
import json

app = Flask(__name__)

@app.route("/")
def movie():
    return "<p>Movies list</p>"


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "2291b34504msh32e737e169ea76ap1def00jsn4ee3554760e2",
    'X-RapidAPI-Host': "imdb8.p.rapidapi.com"
    }
# Obtenir la liste des id des acteurs nés aujourd'hui :
conn.request("GET", "/actors/list-born-today?month=7&day=27", headers=headers)

res = conn.getresponse()
data = res.read()

list_id = data.decode("utf-8")

x = json.loads(list_id)

dict_name = {}

# Obtenir nom prénom des acteurs à partir de leur id :
for id in x[:1] :

    id = id.split('/')[-2]
    conn.request("GET", "/actors/get-bio?nconst=" + str(id), headers=headers)
    res = conn.getresponse()
    data = res.read()
    list_bio = data.decode("utf-8")
    json_bio= json.loads(list_bio)
    name = json_bio['name']
    dict_name[id] = name

print(dict_name)

id = x[3].split('/')[-2]

print('id = ' +str(id) + '\n')

# Obtenir award, détail d'un acteur, image à partir de son id (et afficher son nom, prénom)

conn.request("GET", "/actors/get-awards-summary?nconst=" + str(id), headers=headers)

res = conn.getresponse()
data = res.read()

#Récupérer les award

awards = data.decode("utf-8")

json_awards= json.loads(awards)
#name = json_bio['name']
try:
    print(json_awards['awardsSummary']['highlighted']['awardName'])
    award = json_awards['awardsSummary']['highlighted']['awardName']
    
except KeyError:
    print("Pas d'award")
    award = "Pas d'award"

print('\n')

# Photo acteur :
conn.request("GET", "/actors/get-bio?nconst=" + str(id), headers=headers)
res = conn.getresponse()

data = res.read()
detail = data.decode("utf-8")
json_detail= json.loads(awards)
url_image = json_detail['image']['url']

print('\n')
print(url_image)