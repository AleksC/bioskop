import json
from provere import unos_broja, provera_poklapanja
from rad_sa_fajlovima import ucitavanje_podataka

zanrovi = ucitavanje_podataka("../data/zanrovi.json")
filmovi = ucitavanje_podataka("../data/filmovi.json")

def izbor_zanra(): 
    '''
    Biranje zanra od podstojecih koji se ucitavaju iz fajla.
    '''
    while True:
        try:
            print("Izaberite jedan od ponudjenih zanrova: ")
            for i in range(1, len(zanrovi)+1):
                print(str(i) + " - " + zanrovi[i-1])            
            izbor = int(input("Vas izbor: "))
            return zanrovi[izbor-1]
        except ValueError:
            print("Molimo unesite broj ispred imena zeljenog zanra.")
        except IndexError:
            print("Izabrali ste nepostojeci zanr. Molimo da odaberete neki od ponudjenih.")

def unos_filma():
    '''
    Upisivanje novog filma u listu filmova.
    '''
    ime_filma = input("Molimo unesite ime filma: ")
    zanr = izbor_zanra()
    duzina = unos_broja("Molimo unesite duzinu filma u minutama: ")
    while duzina < 1:
        print("Film mora trajati duze od jednog minuta.")
        duzina = unos_broja("Molimo unesite duzinu filma u minutama: ")
    unet_film = {"id": str(len(filmovi)), "ime": ime_filma, "zanr": zanr, "duzina": str(duzina)}
    with open('../data/filmovi.json', 'w') as fajl:
        filmovi.append(filmovi.append(unet_film))
        filmovi.pop()
        json.dump(filmovi, fajl)

