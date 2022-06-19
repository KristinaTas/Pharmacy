import racuniIO
import lekoviIO

lekovi = lekoviIO.ucitaj_fajl()
racuni = racuniIO.ucitaj_fajl()

def ukupna_prodaja_svih_lekova(izvestaj):
    for lek in lekovi:
        prodata_kolicina = 0
        for racun in racuni:
            prodata_kolicina = racunanje_prodate_kolicine(lek, racun, prodata_kolicina)
        lek['prodata kolicina'] = prodata_kolicina
        lek['zarada'] = lek['cena'] * prodata_kolicina
        izvestaj.append(lek)
    return izvestaj

def ukupna_prodaja_lekova_proizvodjac(proizvodjac, izvestaj):
    for lek in lekovi:
        if proizvodjac.title() in lek['proizvodjac'] or proizvodjac.lower() in lek['proizvodjac']:
            prodata_kolicina = 0
            for racun in racuni:
                prodata_kolicina = racunanje_prodate_kolicine(lek, racun, prodata_kolicina)
            lek['prodata kolicina'] = prodata_kolicina
            lek['zarada'] = lek['cena'] * prodata_kolicina
            izvestaj.append(lek)
    return izvestaj

def ukupna_prodaja_lekova_apotekar(apotekar, izvestaj):
    for lek in lekovi:
        prodata_kolicina = 0
        for racun in racuni:
            if apotekar.title() in racun['apotekar'] or apotekar.lower() in racun['apotekar']:
                prodata_kolicina = racunanje_prodate_kolicine(lek, racun, prodata_kolicina)
        if prodata_kolicina != 0:
            lek['prodata kolicina'] = prodata_kolicina
            lek['zarada'] = lek['cena'] * prodata_kolicina
            izvestaj.append(lek)
    return izvestaj

def racunanje_prodate_kolicine(lek, racun, prodata_kolicina):
    for stavka in range(0, len(racun['lekovi i kolicina'])):
        if lek['ime'] == racun['lekovi i kolicina'][stavka]['lek']:
            prodata_kolicina += racun['lekovi i kolicina'][stavka]['kolicina']
    return prodata_kolicina