import korisnici
import lekovi
import recepti
import izvestaji
import prodaja_lekova


def prijava_na_sistem():
    brojac = 0
    while True:
        korisnicko_ime = input('Korisničko ime: ')
        lozinka = input('Lozinka: ')
        brojac += 1
        korisnik = korisnici.autentikacija(korisnicko_ime, lozinka)
        if korisnik:
            return korisnik
        if brojac >= 3:
            return None
        else:
            print('\nGreška! Uneli ste pogrešno korisničko ime i/ili lozinku. Pokušajte ponovo.')


def prikaz_menija(ulogovan_korisnik):
    meni_svi_korisnici()
    if ulogovan_korisnik['tip korisnika'] == 'Administrator' or ulogovan_korisnik['tip korisnika'] == 'Apotekar':
        meni_administratori_apotekari()
        if ulogovan_korisnik['tip korisnika'] == 'Administrator':
            meni_administratori()
        elif ulogovan_korisnik['tip korisnika'] == 'Apotekar':
            meni_apotekari()
    elif ulogovan_korisnik['tip korisnika'] == 'Lekar':
        meni_lekari()
    komanda = input('Komanda: ')
    return komanda

def funkcionalnosti(ulogovan_korisnik, komanda):
    funkcionalnosti_svi_korisnici(komanda, ulogovan_korisnik)
    if ulogovan_korisnik['tip korisnika'] == 'Administrator' or ulogovan_korisnik['tip korisnika'] == 'Apotekar':
        funkcionalnosti_administratori_apotekari(komanda, ulogovan_korisnik)
        if ulogovan_korisnik['tip korisnika'] == 'Administrator':
            funkcionalnosti_administratori(komanda)
        elif ulogovan_korisnik['tip korisnika'] == 'Apotekar':
            funkcionalnosti_apotekari(komanda, ulogovan_korisnik)
    elif ulogovan_korisnik['tip korisnika'] == 'Lekar':
        funkcionalnosti_lekari(komanda, ulogovan_korisnik)


def funkcionalnosti_svi_korisnici(komanda, ulogovan_korisnik):
    if komanda == '1':
        prikaz_sortiranih_lekova(ulogovan_korisnik)
    elif komanda == '2':
        pretraga_lekova_po_parametru(ulogovan_korisnik)
    elif komanda == '3':
        prikaz_sortiranih_recepata()
    elif komanda == '4':
        pretraga_recepta_po_parametru()

def funkcionalnosti_administratori_apotekari(komanda, ulogovan_korisnik):
    if komanda == '5':
        dodavanje_novog_leka(ulogovan_korisnik)
    elif komanda == '6':
        izmena_postojeceg_leka(ulogovan_korisnik)
    elif komanda == '7':
        logicko_brisanje_leka(ulogovan_korisnik)

def funkcionalnosti_administratori(komanda):
    if komanda == '8':
        registracija_novog_korisnika()
    elif komanda == '9':
        prikaz_sortiranih_korisnika()
    elif komanda == '10':
        kreiranje_izvestaja()

def funkcionalnosti_apotekari(komanda, ulogovan_korisnik):
    if komanda == '8':
        prodavanje_lekova(ulogovan_korisnik)

def funkcionalnosti_lekari(komanda, ulogovan_korisnik):
    if komanda == '5':
        kreiranje_recepta(ulogovan_korisnik)


def prikaz_sortiranih_lekova(ulogovan_korisnik):
    izbor_kriterijuma_za_sortiranje_lekova()
    izbor = eval(input('Izbor: '))
    lista_lekova = lekovi.sortiranje_lekova(izbor, lekovi.lekovi_za_prikaz(ulogovan_korisnik))
    tabela_lekova(lista_lekova)

def pretraga_lekova_po_parametru(ulogovan_korisnik):
    izbor_parametra_za_pretragu_lekova()
    izbor = eval(input('Izbor: '))
    if izbor == 1:
        sifra = input('\nUnesite željenu šifru: ')
        lista_lekova = lekovi.pronalazenje_leka_po_sifri(sifra, lekovi.lekovi_za_prikaz(ulogovan_korisnik))
        tabela_lekova(lista_lekova)
    elif izbor == 2:
        ime = input('\nUnesite željeno ime: ')
        lista_lekova = lekovi.pronalazenje_leka_po_imenu(ime, lekovi.lekovi_za_prikaz(ulogovan_korisnik))
        tabela_lekova(lista_lekova)
    elif izbor == 3:
        proizvodjac = input('\nUnesite željenog proizvođača: ')
        lista_lekova = lekovi.pronalazenje_leka_po_proizvodjacu(proizvodjac, lekovi.lekovi_za_prikaz(ulogovan_korisnik))
        tabela_lekova(lista_lekova)
    elif izbor == 4:
        donja_granica = eval(input('\nUnesite donju granicu opsega: '))
        gornja_granica = eval(input('Unesite gornju granicu opsega: '))
        lista_lekova = lekovi.pronalazenje_leka_po_ceni(donja_granica, gornja_granica, lekovi.lekovi_za_prikaz(ulogovan_korisnik))
        tabela_lekova(lista_lekova)

def prikaz_sortiranih_recepata():
    izbor_kriterijuma_za_sortiranje_recepata()
    izbor = eval(input('Izbor: '))
    lista_recepata = recepti.sortiranje_recepata(izbor)
    tabela_recepata(lista_recepata)

def pretraga_recepta_po_parametru():
    izbor_parametra_za_pretragu_recepata()
    izbor = eval(input('Izbor: '))
    if izbor == 1:
        sifra = eval(input('\nUnesite željenu šifru: '))
        lista_recepata = recepti.pronalazenje_recepata_po_sifri(sifra)
        tabela_recepata(lista_recepata)
    elif izbor == 2:
        lekar = input('\nUnesite željenog lekara: ')
        lista_recepata = recepti.pronalazenje_recepata_po_lekaru(lekar)
        tabela_recepata(lista_recepata)
    elif izbor == 3:
        jmbg = input('\nUnesite JMBG pacijenta: ')
        lista_recepata = recepti.pronalazenje_recepata_po_jmbgu(jmbg)
        tabela_recepata(lista_recepata)
    elif izbor == 4:
        lek = input('\nUnesite željeni lek: ')
        lista_recepata = recepti.pronalazenje_recepata_po_leku(lek)
        tabela_recepata(lista_recepata)

def dodavanje_novog_leka(ulogovan_korisnik):
    while True:
        sifra = input('\nUnesite šifru: ')
        if not lekovi.provera_sifre_leka(sifra, ulogovan_korisnik):
            ime = input('Unesite ime: ')
            proizvodjac = input('Unesite proizvođača: ')
            while True:
                izdaje_se_na_recept = input('Da li se izdaje na recept? ')
                if izdaje_se_na_recept.capitalize() != 'Da' and izdaje_se_na_recept.capitalize() != 'Ne':
                    print('Unesite "Da" ili "Ne"!')
                else:
                    break
            cena = eval(input('Unesite cenu: '))
            lekovi.dodavanje_lekova(sifra, ime, proizvodjac, izdaje_se_na_recept, cena)
            print('Uspešno ste dodali lek.')
            break
        else:
            print('Već postoji lek sa šifrom koju ste uneli! Pokušajte ponovo.')

def izmena_postojeceg_leka(ulogovan_korisnik):
    while True:
        sifra = input('\nUnesite šifru leka čije podatke želite da izmenite: ')
        if lekovi.provera_sifre_leka(sifra, ulogovan_korisnik):
            print('Ako se neki podatak ne menja samo pritisnite enter. Šifru nije moguće menjati!')
            ime = input('Unesite novo ime: ')
            proizvodjac = input('Unesite novog proizvođača: ')
            while True:
                izdaje_se_na_recept = input('Da li se izdaje na recept? ')
                if izdaje_se_na_recept.capitalize() != 'Da' and izdaje_se_na_recept.capitalize() != 'Ne' and izdaje_se_na_recept != '':
                    print('Unesite "Da" ili "Ne"!')
                else:
                    break
            cena = input('Unesite novu cenu: ')
            lekovi.izmena_leka(sifra, ime, proizvodjac, izdaje_se_na_recept, cena, ulogovan_korisnik)
            print('Uspešno ste izmenili lek.')
            break
        else:
            print('Ne postoji lek sa tom šifrom! Pokušajte ponovo.')

def logicko_brisanje_leka(ulogovan_korisnik):
    while True:
        sifra = input('\nUnesite šifru leka koji želite da obrišete: ')
        if lekovi.provera_sifre_leka(sifra, ulogovan_korisnik):
            lekovi.logicko_brisanje_lekova(sifra, ulogovan_korisnik)
            print('Uspešno ste obrisali lek.')
            break
        else:
            print('Greška! Uneli ste šifru koja ne postoji.')

def registracija_novog_korisnika():
    while True:
        tip_korisnika = input('\nUnesite tip korisnika: ')
        if korisnici.provera_tipa_korisnika(tip_korisnika):
            while True:
                korisnicko_ime = input('Unesite korisničko ime: ')
                if korisnici.provera_korisnickog_imena(korisnicko_ime):
                    lozinka = input('Unesite lozinku: ')
                    ime = input('Unesite ime: ')
                    prezime = input('Unesite prezime: ')
                    korisnici.registracija(korisnicko_ime, lozinka, ime, prezime, tip_korisnika)
                    print('Uspešno ste registrovali novog korisnika.')
                    return False
                else:
                    print('\nVeć postoji korisnik sa tim korisničkim imenom. Pokušajte ponovo.')
        else:
            print('Greška! Možete da registujete samo lekare i apotekare.')

def prikaz_sortiranih_korisnika():
    izbor_kriterijuma_za_sortiranje_korisnika()
    izbor = eval(input('Izbor: '))
    lista_korisnika = korisnici.prikaz_korisnika(izbor)
    tabela_korisnika(lista_korisnika)

def kreiranje_izvestaja():
    izvestaj = []
    izbor_vrste_izvestaja()
    izbor = eval(input('Izbor: '))

    if izbor == 1:
        izvestaj = izvestaji.ukupna_prodaja_svih_lekova(izvestaj)
    elif izbor == 2:
        proizvodjac = input('\nUnesite željenog proizvođača: ')
        izvestaj = izvestaji.ukupna_prodaja_lekova_proizvodjac(proizvodjac, izvestaj)
    elif izbor == 3:
        apotekar = input('\nUnesite željenog apotekara: ')
        izvestaj = izvestaji.ukupna_prodaja_lekova_apotekar(apotekar, izvestaj)
    prikaz_izvestaja(izvestaj)

def prodavanje_lekova(ulogovan_korisnik):
    korpa = []
    while True:
        prikaz_nacina_kupovine()
        opcija = eval(input('Izbor: '))

        if opcija == 1:
            korpa = prodaja_sifrom_leka(korpa, ulogovan_korisnik)
        elif opcija == 2:
            korpa = prodaja_receptom(korpa)
        elif opcija == 3:
            break
        else:
            print('Greška! Izabrali ste opciju koja ne postoji.')

        if korpa:
            izbor = nastavak_kupovine(ulogovan_korisnik, korpa)
            if izbor == 3 or izbor == 4:
                return False

def prodaja_sifrom_leka(korpa, ulogovan_korisnik):
    print('\nUnesite šifru leka i količinu koja se kupuje. Ne smete da unesete lek koji se izdaje na recept!')
    while True:
        sifra_leka = input('Šifra: ')
        lek = lekovi.provera_sifre_leka(sifra_leka, ulogovan_korisnik)
        if lek:
            if lekovi.provera_izdavanja_leka_na_recept(lek):
                kolicina = eval(input('Količina: '))
                korpa = prodaja_lekova.prodaja_lekova_sifra(sifra_leka, kolicina, korpa)
                odgovor = input('Da li želite da unesete još lekova (Da/Ne)? ')

                if odgovor.capitalize() == 'Ne':
                    break
            else:
                print('Greška! Uneli ste lek koji se izdaje na recept.')
        else:
            print('Greška! Ne postoji lek sa tom šifrom.')
    return korpa

def prodaja_receptom(korpa):
    while True:
        sifra_recepta = eval(input('\nUnesite šifru recepta: '))
        recept = recepti.provera_sifre_recepta(sifra_recepta)
        if recept:
            korpa = prodaja_lekova.prodaja_lekova_recept(sifra_recepta, korpa)
            return korpa
        else:
            print('Greška! Ne postoji recept sa tom šifrom.')

def nastavak_kupovine(ulogovan_korisnik, korpa):
    while True:
        prikaz_nastavka_kupovine()
        izbor = eval(input('Izbor: '))

        if izbor == 1:
            tabela_korpa(korpa)
        elif izbor == 2 or izbor == 3:
            break
        elif izbor == 4:
            prodaja_lekova.kreiranje_racuna(ulogovan_korisnik, korpa)
            break
        else:
            print('Greška! Izabrali ste opciju koja ne postoji.')
    return izbor

def kreiranje_recepta(ulogovan_korisnik):
    jmbg_pacijenta = input('\nUnesite JMBG pacijenta: ')
    lekovi_i_kolicina = []
    while True:
        recept = {}
        lek = input('Unesite lek: ')
        recept['lek'] = lek.capitalize()
        recept['kolicina'] = input('Unesite količinu: ')
        lekovi_i_kolicina.append(recept)
        odgovor = input('Da li želite da unesete još lekova (Da/Ne)? ')

        if odgovor.capitalize() == 'Ne':
            recepti.kreiranje_recepta(ulogovan_korisnik, jmbg_pacijenta, lekovi_i_kolicina)
            return False


def meni_svi_korisnici():
    print('\n1) Prikaz svih lekova')
    print('2) Pretraga lekova')
    print('3) Prikaz svih recepata')
    print('4) Pretraga recepata')

def meni_administratori_apotekari():
    print('5) Dodavanje lekova')
    print('6) Izmena lekova')
    print('7) Logičko brisanje lekova')

def meni_administratori():
    print('8) Registracija novog korisnika')
    print('9) Prikaz svih korisnika')
    print('10) Kreiranje izveštaja')
    print('x) Kraj programa')

def meni_apotekari():
    print('8) Prodaja lekova')
    print('x) Kraj programa')

def meni_lekari():
    print('5) Kreiranje recepta')
    print('x) Kraj programa')


def izbor_kriterijuma_za_sortiranje_korisnika():
    print('\nIzaberite kriterijum za sortiranje korisnika:')
    print('1) ime')
    print('2) prezime')
    print('3) tip korisnika')

def izbor_kriterijuma_za_sortiranje_lekova():
    print('\nIzaberite kriterijum za sortiranje lekova:')
    print('1) ime')
    print('2) proizvođač')
    print('3) cena')

def izbor_parametra_za_pretragu_lekova():
    print('\nIzaberite parametar za pretragu lekova:')
    print('1) šifra')
    print('2) ime')
    print('3) proizvođač')
    print('4) opseg cene')

def izbor_kriterijuma_za_sortiranje_recepata():
    print('\nIzaberite kriterijum za sortiranje recepata:')
    print('1) šifra')
    print('2) lekar')
    print('3) datum')

def izbor_parametra_za_pretragu_recepata():
    print('\nIzaberite parametar za pretragu recepata:')
    print('1) šifra')
    print('2) lekar')
    print('3) jmbg pacijenta')
    print('4) jedan lek')

def izbor_vrste_izvestaja():
    print('\nVrsta izveštaja:')
    print('1) ukupna prodaja svih lekova')
    print('2) ukupna prodaja lekova jednog proizvođača')
    print('3) ukupna prodaja lekova koje je prodao jedan apotekar')


def prikaz_nacina_kupovine():
    print('\n1) Kupovina unošenjem šifre leka')
    print('2) Kupovina unošenjem šifre recepta')
    print('3) Odustani od kupovine')

def prikaz_nastavka_kupovine():
    print('\nVaš sledeći korak:')
    print('1) Pregled korpe')
    print('2) Nastavak kupovine')
    print('3) Odustani od kupovine')
    print('4) Potvrda kupovine')


def tabela_lekova(lista_lekova):
    print("{:<10}{:<20}{:<20}{:<25}{:<15}".format('\nŠifra', 'Ime', 'Proizvođač', 'Izdaje se na recept', 'Cena'))
    print("-" * 90)
    for lek in lista_lekova:
        print("{:<10}{:<20}{:<20}{:<25}{:<15}".format(lek['sifra'], lek['ime'], lek['proizvodjac'], lek['izdaje se na recept'], lek['cena']))

    print("-" * 90)

def tabela_recepata(lista_recepata):
    print("{:<10}{:<20}{:<20}{:<20}{:<30}".format('\nŠifra', 'Lekar', 'JMBG pacijenta', 'Datum i vreme', 'Lekovi i količina'))
    print("-" * 100)
    for recept in lista_recepata:
        print("{:<10}{:<20}{:<20}{:<20}{:<30}".format(recept['sifra'], recept['lekar'], recept['jmbg pacijenta'], recept['datum i vreme'], recept['lekovi i kolicina string']))

    print("-" * 100)

def tabela_korisnika(lista_korisnika):
    print("{:<20}{:<20}{:<20}{:<20}".format('\nKorisničko ime', 'Ime', 'Prezime', 'Tip korisnika'))
    print("-" * 80)
    for korisnik in lista_korisnika:
        print("{:<20}{:<20}{:<20}{:<20}".format(korisnik['korisnicko ime'], korisnik['ime'], korisnik['prezime'], korisnik['tip korisnika']))

    print("-" * 80)

def prikaz_izvestaja(izvestaj):
    print("{:<10}{:<20}{:<20}{:<25}{:<15}{:<20}{:<15}".format('\nŠifra', 'Ime', 'Proizvođač', 'Izdaje se na recept', 'Cena', 'Prodata količina', 'Zarada'))
    print("-" * 130)
    for red in izvestaj:
        print("{:<10}{:<20}{:<20}{:<25}{:<15}{:<20}{:<15}".format(red['sifra'], red['ime'], red['proizvodjac'], red['izdaje se na recept'], red['cena'], red['prodata kolicina'], red['zarada']))

    print("-" * 125)

def tabela_korpa(korpa):
    ukupan_iznos = 0
    print(
        "{:<10}{:<20}{:<20}{:<25}{:<15}{:<10}".format('\nŠifra', 'Ime', 'Proizvođač', 'Izdaje se na recept', 'Cena', 'Količina'))
    print("-" * 100)
    for lek in korpa:
        print("{:<10}{:<20}{:<20}{:<25}{:<15}{:<10}".format(lek['sifra'], lek['ime'], lek['proizvodjac'], lek['izdaje se na recept'], lek['cena'], lek['kolicina']))
        ukupan_iznos += lek['cena'] * lek['kolicina']

    print("-" * 100)
    print('Ukupan iznos: ', ukupan_iznos)


def main():
    print('Unesite korisničko ime i lozinku.')
    ulogovan_korisnik = prijava_na_sistem()
    if ulogovan_korisnik:
        while True:
            komanda = prikaz_menija(ulogovan_korisnik)
            if komanda.lower() == 'x':
                break
            else:
                funkcionalnosti(ulogovan_korisnik, komanda)

if __name__ == "__main__":
    main()