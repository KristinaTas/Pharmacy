import korisniciIO

korisnici = korisniciIO.ucitaj_fajl()

def autentikacija(korisnicko_ime, lozinka):
    for korisnik in korisnici:
        if korisnicko_ime == korisnik['korisnicko ime'] and lozinka == korisnik['lozinka']:
            return korisnik
    return None

def provera_korisnickog_imena(korisnicko_ime):
    for korisnik in korisnici:
        if korisnik['korisnicko ime'] == korisnicko_ime:
            return False
    return True

def provera_tipa_korisnika(tip_korisnika):
    if tip_korisnika.capitalize() == 'Lekar' or tip_korisnika.capitalize() == 'Apotekar':
        return True
    else:
        return False

def registracija(korisnicko_ime, lozinka, ime, prezime, tip_korisnika):
    korisnik = {}
    korisnik['korisnicko ime'] = korisnicko_ime
    korisnik['lozinka'] = lozinka
    korisnik['ime'] = ime.title()
    korisnik['prezime'] = prezime.title()
    korisnik['tip korisnika'] = tip_korisnika.capitalize()
    korisnici.append(korisnik)
    korisniciIO.sacuvaj_u_fajl(korisnici)

def prikaz_korisnika(izbor):
    if izbor == 1:
        korisnici.sort(key=lambda x: x['ime'])
    elif izbor == 2:
        korisnici.sort(key=lambda x: x['prezime'])
    elif izbor == 3:
        korisnici.sort(key=lambda x: x['tip korisnika'])
    return korisnici