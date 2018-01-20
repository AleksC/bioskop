from projekcije import projekcije, unos_broja
from rad_sa_fajlovima import ucitavanje_podataka
import json
from datetime import datetime


def trenutno_vreme():
    '''
    Funkcija koja vraca trenutno vreme u obliku stringa.
    '''
    trenutno_vreme = datetime.today().strftime("%Y-%m-%d %H:%M").split()
    datum = trenutno_vreme[0].split("-")
    datum = datum[2] + " " + datum[1] + " " + datum[0]
    vreme = trenutno_vreme[1].split(":")
    vreme = vreme[0] + " " + vreme[1]
    return vreme, datum

def prodaja_karata(projekcija):
    while True:
        print("0 - Povratak na prethodni meni")
        broj_karata = unos_broja("Molimo odaberite koliko karata zelite da prodate (0 za povratak na prethodni meni): ")
        if broj_karata == 0:
            break 
        elif int(projekcija["broj_slobodnih_mesta"]) < broj_karata:
            print("Odabrali ste vise karata nego postoji slobodno.")
            print("Molimo odaberite broj manji od " + projekcija["broj_slobodnih_mesta"])
        elif int(projekcija["broj_ukupnih_mesta"]) < broj_karata:
            print("Za ovu projekciju ne postoji tolika kolicina karata zbog ogranicenja sale.")
            print("Molimo odaberite broj manji od " + projekcija["broj_ukupnih_mesta"])
        else:
            return broj_karata, projekcija

def izdavanje_racuna(ukupna_cena, broj_karata, projekcija, sve_projekcije):
    '''
    Prolazak kroz razlicite opcije. Upisuje u fajl novi racun ako se kreira,
    u suprotnom vraca informacije o broju prodatih karata, kao i za koje projekcije 
    su prodate. Ukoliko je racun izdata, ili otkazan, funkcija resetuje pocetne argumente.
    U suporotnom prosledjuje modifikovane argumente.
    '''
    while True:
        trenutna_cena = broj_karata * float(projekcija["cena"])
        print("Vas racun je: " + str(trenutna_cena) + " dinara.")
        print("Da li zelite da odstampate racun?")
        print("1 - Da")
        print("2 - Ne (prodaja karata za druge projekcije)")
        print("3 - Ne (ponistavanje racuna)")
        izbor = unos_broja()
        ukupna_cena += trenutna_cena
        if izbor == 1:
            racuni = ucitavanje_podataka("../data/racuni.json")
            #smanjivanje broja slobodnih mesta u projekciji (ili projekcijama)
            with open('../data/projekcije.json', 'w') as fajl:
                for i in sve_projekcije:
                    indeks = int(i["id"])-1
                    projekcije[indeks]["broj_slobodnih_mesta"] = str(int(projekcije[indeks]["broj_slobodnih_mesta"]) - broj_karata)
                json.dump(projekcije, fajl)
            #dodavanje racuna
            with open('../data/racuni.json', 'w') as f: 
                vreme, datum = trenutno_vreme()
                konacan_racun = {"sifra": str(len(racuni)), "vreme": vreme, "datum": datum, "ukupna_cena": str(ukupna_cena)}
                racuni.append(konacan_racun)
                json.dump(racuni, f)
            print("Karte uspesno prodate!")
            return 0, 0, False, []
        elif izbor == 2:
            with open('../data/projekcije.json', 'w') as fajl:
                for i in sve_projekcije:
                    indeks = int(i["id"])-1
                    projekcije[indeks]["broj_slobodnih_mesta"] = str(int(projekcije[indeks]["broj_slobodnih_mesta"]) - broj_karata)
                json.dump(projekcije, fajl)
            return ukupna_cena, broj_karata, projekcija, []
        elif izbor == 3:    
            with open('../data/projekcije.json', 'w') as fajl:        
                for i in sve_projekcije:
                    indeks = int(i["id"])-1
                    projekcije[indeks]["broj_slobodnih_mesta"] = str(int(projekcije[indeks]["broj_slobodnih_mesta"]) + broj_karata)
                json.dump(projekcije, fajl)
            return 0, 0, False, []
        else:
            print("Molimo unesite jednu od ponudjenih opcija.") 

def racun():
    '''
    Glavni meni za racun. Vodi evidenciju o ukupnom broju karata,
    kao i o ukupnoj ceni, i za koje projekcije su prodate.
    '''
    broj_karata = 0
    ukupna_cena = 0
    izabrana_projekcija = False
    sve_projekcije = []
    while True: 
        projekcije = ucitavanje_podataka("../data/projekcije.json")
        print("Odaberite opciju: ")
        print("1 - Prodaja karata")
        print("2 - Izdavanje racuna")
        print("0 - Povratak na prethodni meni")
        unos = unos_broja()
        if unos == 0:
            break
        elif unos == 1:
            while True:
                print("Molimo odaberite za koju projekciju zelite da prodate kartu.")
                for i in projekcije:
                    print(str(i["id"]) + " - " + i["film"] + " | " + str(i["datum"]) + " u " + str(i["vreme"]) + " | Slobodnih mesta: " + str(i["broj_slobodnih_mesta"]))
                print("0 - Povratak na prethodni meni")
                izbor = unos_broja()
                if izbor == 0:
                    break
                elif izbor > len(projekcije):
                    print("Odabrana nepostojeca projekcija.")
                else:
                    izabrana_projekcija = projekcije[izbor-1]
                    sve_projekcije.append(izabrana_projekcija)
                    try:
                        broj_prodatih_karata, izabrana_projekcija = prodaja_karata(izabrana_projekcija)
                        broj_karata += broj_prodatih_karata
                    except TypeError:
                        print("Projekcija nije odabrana.")
        elif unos == 2:
            if izabrana_projekcija != False:
                ukupna_cena, broj_karata, izabrana_projekcija, sve_projekcije = izdavanje_racuna(ukupna_cena, broj_karata, izabrana_projekcija, sve_projekcije)
            else:
                print("Molimo prvo odaberite projekciju za koju zelite da prodate kartu.")
            
racun()