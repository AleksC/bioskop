from datetime import datetime

#dozvoljeni tipovi zanra, od veceg znacaja za drugi deo projekta kada se doda funkcija dodavanja filmova
zanrovi = ["sci-fi", "fantasy", "action", "thriller", "horror"]

#primeri filmova
filmovi = [{"id": 0,
            "ime": "Star Wars",
            "zanr": zanrovi[0]
            },
           {"id": 1,
            "ime": "Harry Potter",
            "zanr": zanrovi[1]
            }]

#definisane sale radi automatskog dodeljivanja broja ukupnih i slobodnih mesta novoj projekciji
sale = [{"ime_sale": "A1",
         "kapacitet": 150},
        {"ime_sale": "A2",
         "kapacitet": 200},
        {"ime_sale": "B1",
         "kapacitet": 80},
        {"ime_sale": "B2",
         "kapacitet": 95}]

#primer projekcije
projekcije = [{"id": 0,
               "datum": datetime.strptime("11 11 2017", "%d %m %Y").date(),
               "vreme": datetime.strptime("21 00", "%H %M").time(),
               "duzina": 120,
               "cena": 300.0,
               "film": filmovi[0]["ime"],
               "sala": sale[0]["ime_sale"],
               "obrisana": False,
               "broj_slobodnih_mesta": 200,
               "broj_ukupnih_mesta": 250
               }]


def unos_datuma(): #Funkcija koja proverava da li je datum unesen u ispravnom formatu
    while True:
        try:
            datum = input("Unesite datum projkecije u formatu dd mm yyyy: ")
            datum = datetime.strptime(datum, "%d %m %Y").date()
            break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return datum        

def unos_vremena(): #Funkcija koja proverava da li je vreme uneseno u ispravnom formatu
    while True:
        try:
            vreme = input("Unesite vreme projkecije u formatu hh mm: ")
            vreme = datetime.strptime(vreme, "%H %M").time()
            break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return vreme

def unos_duzine():
    """Funkcija za dodavanje duzine projekcije.
    Ovaj deo planiram da promenim za drugi deo projekta,
    tako da se duzina projekcija dodaje pri unosu filma
    i automatski dodeljuje projekciji tog filma kada se ona kreira."""
    return unos_broja("Unesite duzinu trajanja projkecije u minutima: ") #poziv funkcije koja proverava da li je unet broj

def izbor_zanra(): #Funkcija za izbor zanra koja ce se koristiti kada se bude unosio film u drugom delu projekta
    while True:
        try:
            print("Izaberite jedan od ponudjenih zanrova: ")
            for i in range(len(zanrovi)):
                print(str(i) + " - " + zanrovi[i])            
            izbor = int(input("Vas izbor: "))
            return zanrovi[izbor]
        except ValueError:
            print("Molimo unesite broj ispred imena zeljenog zanra.")
        except IndexError:
            print("Izabrali ste nepostojeci zanr. Molimo da odaberete neki od ponudjenih.")
            
def izbor_sale(): #Funkcija za odabir sale
    while True:
        try:
            print("Izaberite salu u kojoj ce se odrzavati projekcija: ")
            for i in range(len(sale)):
                print(str(i) + " - " + sale[i]["ime_sale"])
            izbor = int(input("Vas izbor: "))
            return sale[izbor]
        except ValueError:
            print("Molimo unesite broj ispred imena sale.")
        except IndexError:
            print("Izabrali ste nepostojecu salu. Molimo da odaberete neki od ponudjenih.")
            

def unos_filma(): #Za prvi deo projekta nije omogucena
    print("Ova opcija nije omogucena.")

def izbor_filma():
    print("Izaberite jedan od ponudjenih filmova: ")
    izbor = None
    for i in range(len(filmovi)):
        print(str(i) + " - " + filmovi[i]["ime"])
    print(str(i + 1) + " - Unos novog filma")
    while True:
        try:
            izbor = int(input("Vas izbor: "))
            izbor = filmovi[izbor]
            break
        except ValueError:
            print("Molimo unesite broj ispred imena zeljenog filma.")
        except IndexError:
            if izbor == len(filmovi):
                print("Ova opcija nije omogucena.")
            else:
                print("Izabrali ste nepostojeci film. Ukoliko zelite da dodate novi film pritisnite " + str(len(filmovi)))
    return izbor

def unos_projekcije(): #Funkcija za dodavanje projekcije
    print("Unos nove projekcije: ")
    datum = unos_datuma()
    vreme = unos_vremena()
    duzina = unos_duzine()
    film = izbor_filma()
    sala = izbor_sale()
    broj_slobodnih_mesta = sala["kapacitet"]
    broj_ukupnih_mesta = sala["kapacitet"]
    #Pridruzivanje unetih podataka u listu kao recnik
    projekcije.append({"id": len(projekcije), "datum": datum, "vreme": vreme, "duzina": duzina, "film": film["ime"], "sala": sala["ime_sale"], "obrisana": False, "broj_slobodnih_mesta": broj_slobodnih_mesta, "broj_ukupnih_mesta": broj_ukupnih_mesta})
    projekcija = len(projekcije)-1
    #Stampanje unetih podataka
    print(""" 
Datum: {0}
Vreme: {1}
Duzina: {2}
Film: {3}
Broj ukupnih mesta: {4}
Broj slobodnih mesta: {5}
Sala: {6}

""".format(projekcije[projekcija]["datum"], projekcije[projekcija]["vreme"], projekcije[projekcija]["duzina"], projekcije[projekcija]["film"], projekcije[projekcija]["broj_ukupnih_mesta"], projekcije[projekcija]["broj_slobodnih_mesta"], projekcije[projekcija]["sala"]))

def pretraga_projekcija(): #Funkcija za pretragu po datim kriterijumima, nije omogucena za prvi deo projekta
    print("Pretrazite projekciju prema:")
    print("1 - ID-u projekcije")
    print("2 - Nazivu filma")
    print("3 - Zanru filma")
    print("4 - Sali prikazivanja")
    unos = unos_broja("Vas izbor: ")
    print("Pretraga projekcija nije omogucena.")
    
def brisanje_projekcije(): #Funkcija za brisanje projekcije, nije omogucena za prvi deo projekta
    print("Odaberite projekciju za brisanje:")
    for projekcija in projekcije:
        print(str(projekcija["id"]) + " - " + projekcija["film"] + " | " + str(projekcija["datum"]) + " u " + str(projekcija["vreme"]))
    unos = unos_broja("Vas izbor: ")
    print("Brisanje projekcije nije omoguceno.")
    '''for projekcija in projekcije:
        if unos == projekcija["id"]:
            projekcija["obrisana"] = True'''
    
def izmena_projekcije(): #Funkcija za izmenu projekcije, nije omogucena za prvi deo projekta
    print("Odaberite projekciju za izmenu.")
    for projekcija in projekcije:
        print(str(projekcija["id"]) + " - " + projekcija["film"] + " | " + str(projekcija["datum"]) + " u " + str(projekcija["vreme"]))
    unos = unos_broja("Vas izbor: ")
    print("Izmena projekcija nije omogucena.")

def unos_broja(tekst): #Pomocna funkcija za ispravan unos broja. Korisiti se uglavnom za izbor stavki u menijima
    while True:
        try:
            unos = int(input(tekst))
            return unos
        except ValueError:
            print("Molimo unesite odgovarajuci broj.")



