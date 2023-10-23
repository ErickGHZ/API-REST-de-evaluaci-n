import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"
response = requests.get(URI)
#print(f"GET: {response.text}")
response_json = json.loads(response.text)
count = response_json["count"]
for i in range(count):
    name = response_json['results'][i]['name']
    print(f"{i+1}.- {name}")

seleccionado = int(input("Escoge un personaje:"))
seleccionado -= 1
name = response_json['results'][seleccionado]['name']
name = name.lower()

URI = f"https://www.dnd5eapi.co/api/classes/{name}"
response = requests.get(URI)
response_json = json.loads(response.text)

proficiencies = response_json.get('proficiencies')
count = len(proficiencies)
for i in range(count):
    proficiencies = response_json['proficiencies'][i]['name']
    print(f"{i+1}. {proficiencies}")



    