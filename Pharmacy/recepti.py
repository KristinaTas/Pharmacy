import receptiIO
from datetime import datetime

def sortiranje_recepata(izbor):
    recepti = receptiIO.ucitaj_fajl()
    if izbor == 1:
        recepti.sort(key=lambda x: x['sifra'])
    elif izbor == 2:
        recepti.sort(key=lambda x: x['lekar'])
    elif izbor == 3:
        recepti.sort(key=lambda x: x['datum i vreme'])

    recepti_za_prikaz = []
    for recept in recepti:
        recepti_za_prikaz = lista_recnika_u_string(recept, recepti_za_prikaz)
    return recepti_za_prikaz


def pronalazenje_recepata_po_sifri(sifra):
    recepti = receptiIO.ucitaj_fajl()
    recepti_za_prikaz = []

    for recept in recepti:
        if str(sifra) in str(recept['sifra']):
            recepti_za_prikaz = lista_recnika_u_string(recept, recepti_za_prikaz)
    return recepti_za_prikaz

def pronalazenje_recepata_po_lekaru(lekar):
    recepti = receptiIO.ucitaj_fajl()
    recepti_za_prikaz = []

    for recept in recepti:
        if lekar.title() in recept['lekar'] or lekar.lower() in recept['lekar']:
            recepti_za_prikaz = lista_recnika_u_string(recept, recepti_za_prikaz)
    return recepti_za_prikaz

def pronalazenje_recepata_po_jmbgu(jmbg):
    recepti = receptiIO.ucitaj_fajl()
    recepti_za_prikaz = []

    for recept in recepti:
        if str(jmbg) in str(recept['jmbg pacijenta']):
            recepti_za_prikaz = lista_recnika_u_string(recept, recepti_za_prikaz)
    return recepti_za_prikaz

def pronalazenje_recepata_po_leku(lek):
    recepti = receptiIO.ucitaj_fajl()
    recepti_za_prikaz = []

    for recept in recepti:
        for jedan in range(0, len(recept['lekovi i kolicina'])):
            if lek.title() in recept['lekovi i kolicina'][jedan]['lek'] or lek.lower() in recept['lekovi i kolicina'][jedan]['lek']:
                recepti_za_prikaz = lista_recnika_u_string(recept, recepti_za_prikaz)
    return recepti_za_prikaz


def kreiranje_recepta(ulogovan_korisnik, jmbg_pacijenta, lekovi_i_kolicina):
    recepti = receptiIO.ucitaj_fajl()
    recept = {}

    recept['sifra'] = len(recepti) + 1
    recept['lekar'] = ulogovan_korisnik['ime'] + ' ' + ulogovan_korisnik['prezime']
    recept['jmbg pacijenta'] = jmbg_pacijenta
    recept['datum i vreme'] = "{:.16}".format(str(datetime.now()))
    recept['lekovi i kolicina'] = lekovi_i_kolicina
    recepti.append(recept)
    receptiIO.sacuvaj_u_fajl(recepti)


def provera_sifre_recepta(sifra):
    recepti = receptiIO.ucitaj_fajl()
    for recept in recepti:
        if recept['sifra'] == sifra:
            return recept
    return None

def lista_recnika_u_string(recept, recepti_za_prikaz):
    kolicina_puta_lek = ''
    for stavka in range(0, len(recept['lekovi i kolicina'])):
        kolicina_puta_lek += str(recept['lekovi i kolicina'][stavka]['kolicina']) + ' x ' + recept['lekovi i kolicina'][stavka]['lek'] + '  '
    recept['lekovi i kolicina string'] = kolicina_puta_lek
    recepti_za_prikaz.append(recept)
    return recepti_za_prikaz