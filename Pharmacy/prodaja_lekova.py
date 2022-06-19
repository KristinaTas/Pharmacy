import lekoviIO
import receptiIO
import racuniIO
from datetime import datetime

racuni = racuniIO.ucitaj_fajl()
lekovi = lekoviIO.ucitaj_fajl()
recepti = receptiIO.ucitaj_fajl()

def prodaja_lekova_sifra(sifra_leka, kolicina, korpa):
    for lek in lekovi:
        if sifra_leka == lek['sifra']:
            lek['kolicina'] = kolicina
            korpa.append(lek)
    return korpa

def prodaja_lekova_recept(sifra_recepta, korpa):
    for recept in recepti:
        if sifra_recepta == recept['sifra']:
            for lek in lekovi:
                for stavka in range(0, len(recept['lekovi i kolicina'])):
                    if lek['ime'] == recept['lekovi i kolicina'][stavka]['lek']:
                        lek['kolicina'] = int(recept['lekovi i kolicina'][stavka]['kolicina'])
                        korpa.append(lek)
    return korpa

def kreiranje_racuna(ulogovan_korisnik, korpa):
    ukupna_cena = 0
    lekovi_i_kolicina = []

    racun = {}
    racun['sifra racuna'] = len(racuni) + 1
    racun['apotekar'] = ulogovan_korisnik['ime'] + ' ' + ulogovan_korisnik['prezime']
    racun['datum i vreme'] = "{:.16}".format(str(datetime.now()))
    for lek in korpa:
        lek_i_kolicina = {'lek' : lek['ime'], 'kolicina' : lek['kolicina']}
        lekovi_i_kolicina.append(lek_i_kolicina)
        ukupna_cena += lek['cena'] * lek_i_kolicina['kolicina']
    racun['lekovi i kolicina'] = lekovi_i_kolicina
    racun['ukupna cena'] = ukupna_cena
    racuni.append(racun)
    racuniIO.sacuvaj_u_fajl(racuni)