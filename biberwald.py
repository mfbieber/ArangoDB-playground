from pyArango.connection import *

import requests

requests.packages.urllib3.disable_warnings()

file = open("haffsonpw", "r")
pw = file.read()

conn = Connection(arangoURL="https://arango.research.haffson.org", username="haffson", password=pw)
db = conn["haffson"]
wald = db.graphs["Biberwald"]

animals = db["Animals"]
cults = db["Cults"]
memberships = db["Memberships"]
likes = db["Likes"]

for collection in [animals, cults, memberships, likes]:
    collection.truncate()

animals = {}
for name in ["Fuchs", "Kaninchen", "Wildschwein", "Einhorn"]:
    animals[name] = wald.createVertex("Animals", {
        "name": name
    })
    print(animals[name])

veggos = wald.createVertex("Cults", {
    "name": "Vegetarier"
})

magicals = wald.createVertex("Cults", {
    "name": "Magische Tiere"
})

# link - in welcher Edge-Collection, von wo, wohin, mit welchen Eigenschaften:
wald.link("Memberships", animals["Fuchs"], veggos, {})
wald.link("Memberships", animals["Einhorn"], magicals, {})
wald.link("Likes", animals["Einhorn"], veggos, {})
wald.link("Likes", animals["Kaninchen"], veggos, {})
wald.link("Likes", animals["Fuchs"], animals["Kaninchen"], {})
wald.link("Likes", animals["Fuchs"], animals["Wildschwein"], {})
wald.link("Likes", animals["Wildschwein"], animals["Fuchs"], {})

# ^ Man kann an jeder Kante/Link/Edge auch noch Eigenschaften speichern (Edges sind
#   in ArangoDB ja auch "Dokumente", also vollwertige Datenbank-Eintraege, aber das
#   Feature benutzen wir hier nicht, deshalb geben wir nur eine leere Map an: {}