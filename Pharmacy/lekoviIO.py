import json

fajl = 'lekovi.json'

def ucitaj_fajl():
    f = open(fajl, 'r')
    lekovi = json.load(f)
    lekovi_za_ucitavanje = []
    for lek in lekovi:
        lek['izdaje se na recept'] = bool_u_string(lek)
        lekovi_za_ucitavanje.append(lek)
    return lekovi_za_ucitavanje

def sacuvaj_u_fajl(lekovi):
    f = open(fajl, 'w')
    json.dump(lekovi, f, indent = 5)

def bool_u_string(lek):
    if lek['izdaje se na recept'] == True:
        return 'Da'
    else:
        return 'Ne'