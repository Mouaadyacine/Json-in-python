import json

data = {
    "nom": "mouaad",
    "age": 18,
    "ville": "marrakech"
}

with open("data.json", "w") as json:
    json.dump(data, json)

with open("data.json", "r") as json:
   data_load = json.load(json)
   print("Contenu du fichier JSON avant modification :")
   print(data_load)

data_load["langage"] = "Python"

with open("data.json", "w") as json:
    json.dump(data_load, json)

with open("data.json", "r") as json:
    modification = json.load(json)
    print("\nContenu du fichier JSON après modification :")
    print(modification)