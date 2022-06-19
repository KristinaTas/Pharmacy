import lekoviIO

def sortiranje_lekova(izbor, lekovi):
    if izbor == 1:
        lekovi.sort(key=lambda x: x['ime'])
    elif izbor == 2:
        lekovi.sort(key=lambda x: x['proizvodjac'])
    elif izbor == 3:
        lekovi.sort(key=lambda x: x['cena'])
    return lekovi


def pronalazenje_leka_po_sifri(sifra, lekovi):
    lekovi_za_prikaz = []

    for lek in lekovi:
        if sifra in lek['sifra']:
            lekovi_za_prikaz.append(lek)
    return lekovi_za_prikaz

def pronalazenje_leka_po_imenu(ime, lekovi):
    lekovi_za_prikaz = []

    for lek in lekovi:
        if ime.lower() in lek['ime'] or ime.title() in lek['ime']:
            lekovi_za_prikaz.append(lek)
    return lekovi_za_prikaz

def pronalazenje_leka_po_proizvodjacu(proizvodjac, lekovi):
    lekovi_za_prikaz = []

    for lek in lekovi:
        if proizvodjac.lower() in lek['proizvodjac'] or proizvodjac.title() in lek['proizvodjac']:
            lekovi_za_prikaz.append(lek)
    return lekovi_za_prikaz

def pronalazenje_leka_po_ceni(donja_granica, gornja_granica, lekovi):
    lekovi_za_prikaz = []

    for lek in lekovi:
        if donja_granica <= lek['cena'] and gornja_granica >= lek['cena']:
            lekovi_za_prikaz.append(lek)
    return lekovi_za_prikaz


def dodavanje_lekova(sifra, ime, proizvodjac, izdaje_se_na_recept, cena):
    lekovi = lekoviIO.ucitaj_fajl()

    for lek in lekovi:
        lek['izdaje se na recept'] = string_u_bool(lek['izdaje se na recept'])
    lek = {}
    lek['sifra'] = sifra
    lek['ime'] = ime.title()
    lek['proizvodjac'] = proizvodjac.title()
    lek['izdaje se na recept'] = string_u_bool(izdaje_se_na_recept)
    lek['cena'] = float(cena)
    lek['obrisan'] = False
    lekovi.append(lek)
    lekoviIO.sacuvaj_u_fajl(lekovi)


def izmena_leka(sifra, ime, proizvodjac, izdaje_se_na_recept, cena, korisnik):
    lekovi = lekovi_za_prikaz(korisnik)

    for lek in lekovi:
        if lek['sifra'] == sifra:
            if ime != '':
                lek['ime'] = ime.title()
            if proizvodjac != '':
                lek['proizvodjac'] = proizvodjac.title()
            if izdaje_se_na_recept != '':
                lek['izdaje se na recept'] = string_u_bool(izdaje_se_na_recept)
            else:
                lek['izdaje se na recept'] = string_u_bool(lek['izdaje se na recept'])
            if str(cena) != '':
                lek['cena'] = float(cena)
        else:
            lek['izdaje se na recept'] = string_u_bool(lek['izdaje se na recept'])
    lekoviIO.sacuvaj_u_fajl(lekovi)


def logicko_brisanje_lekova(sifra, korisnik):
    lekovi = lekovi_za_prikaz(korisnik)

    for lek in lekovi:
        lek['izdaje se na recept'] = string_u_bool(lek['izdaje se na recept'])
        if lek['sifra'] == sifra:
            lek['obrisan'] = True
    lekoviIO.sacuvaj_u_fajl(lekovi)


def provera_sifre_leka(sifra, korisnik):
    lekovi = lekovi_za_prikaz(korisnik)

    for lek in lekovi:
        if lek['sifra'] == sifra:
            return lek
    return None

def provera_izdavanja_leka_na_recept(lek):
    if lek['izdaje se na recept'] == 'Ne':
        return True
    else:
        return False

def string_u_bool(vrednost):
    if vrednost.capitalize() == 'Da':
        return True
    else:
        return False

def lekovi_za_prikaz(korisnik):
    lekovi = lekoviIO.ucitaj_fajl()

    if korisnik['tip korisnika'] == 'Administrator':
        return lekovi
    elif korisnik['tip korisnika'] == 'Apotekar' or korisnik['tip korisnika'] == 'Lekar':
        lekovi_za_prikaz = []
        for lek in lekovi:
            if not lek['obrisan']:
                lekovi_za_prikaz.append(lek)
        return lekovi_za_prikaz