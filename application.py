from flask import Flask, render_template
import http.client
import json

app = Flask(__name__)

@app.route("/")
def movie():
    return "<p>Movies list</p>"


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "732836899fmsh744957c5047c065p117016jsn132cb5d97924",
    'X-RapidAPI-Host': "imdb8.p.rapidapi.com"
    }

conn.request("GET", "/actors/list-born-today?month=7&day=27", headers=headers)

res = conn.getresponse()
data = res.read()

list_id = data.decode("utf-8")

x = json.loads(list_id)

dict_name = {}
for id in x :

    id = id.split('/')[-2]
    conn.request("GET", "/actors/get-bio?nconst=" + str(id), headers=headers)
    res = conn.getresponse()
    data = res.read()
    list_bio = data.decode("utf-8")
    json_bio= json.loads(list_bio)
    name = json_bio['name']
    dict_name[id] = name

print(dict_name)



