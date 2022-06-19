import json

fajl = 'korisnici.json'

def ucitaj_fajl():
    korisnici = open(fajl, 'r')
    return json.load(korisnici)

def sacuvaj_u_fajl(korisnici):
    f = open(fajl, 'w')
    json.dump(korisnici, f, indent = 5)