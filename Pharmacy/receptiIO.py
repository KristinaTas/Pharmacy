import json

fajl = 'recepti.json'

def ucitaj_fajl():
    recepti = open(fajl, 'r')
    return json.load(recepti)

def sacuvaj_u_fajl(recepti):
    f = open(fajl, 'w')
    json.dump(recepti, f, indent = 5)
