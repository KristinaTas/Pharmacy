import json

fajl = 'racuni.json'

def ucitaj_fajl():
    racuni = open(fajl, 'r')
    return json.load(racuni)

def sacuvaj_u_fajl(racuni):
    f = open(fajl, 'w')
    json.dump(racuni, f, indent = 5)