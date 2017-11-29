from datetime import datetime

zanrovi = ["sci-fi", "fantasy", "action", "thriller", "horror"]

filmovi = [{"id": 0,
            "ime": "Star Wars",
            "zanr": "sci-fi"
            },
           {"id": 1,
            "ime": "Harry Potter",
            "zanr": "fantasy"
            }]

projekcije = [{"id": 0,
               "datum": datetime.strptime("11 11 2017", "%d %m %Y").date(),
               "vreme": datetime.strptime("21 00", "%H %M").time(),
               "duzina": 120,
               "cena": 300.0,
               "film": filmovi[0]["ime"],
               "sala": "A1",
               "obrisana": False,
               "broj_slobodnih_mesta": 200,
               "broj_ukupnih_mesta": 250
               }]


def unos_datuma():
    while True:
        try:
            datum = input("Unesite datum projkecije u formatu dd mm yyyy: ")
            datum = datetime.strptime(datum, "%d %m %Y").date()
            break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return datum        

def unos_vremena():
    while True:
        try:
            vreme = input("Unesite vreme projkecije u formatu hh mm: ")
            vreme = datetime.strptime(vreme, "%H %M").time()
            break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return vreme

def unos_duzine():
    while True:
        try:
            duzina = int(input("Unesite duzinu trajanja projkecije u minutima: "))
            break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return duzina

def izbor_zanra():
    while True:
        try:
            print("Izaberite jedan od ponudjenih zanrova: ")
            for i in range(len(zanrovi)):
                print(str(i) + " - " + zanrovi[i])            
            izbor = int(input("Vas izbor: "))
            izbor = zanrovi[izbor]
            break
        except ValueError:
            print("Molimo unesite broj ispred imena zeljenog zanra.")
        except IndexError:
            print("Izabrali ste nepostojeci zanr. Molimo da odaberete neki od ponudjenih.")
    return izbor

def unos_filma():
    print("Ova opcija nije omogucena.")
    return izbor_filma()

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
                izbor = unos_filma
                break
            else:
                print("Izabrali ste nepostojeci film. Ukoliko zelite da dodate novi film pritisnite " + str(len(filmovi)))
    if callable(izbor):
        return izbor()
    else:
        return izbor

def unos_projekcije():
    print("Unos nove projekcije: ")
    datum = unos_datuma()
    vreme = unos_vremena()
    duzina = unos_duzine()
    film = izbor_filma()
    sala = input("Unesite salu projekcije: ")
    broj_slobodnih_mesta = input("Unesite broj slobodnih mesta: ")
    broj_ukupnih_mesta = input("Unesite broj ukupnih mesta: ")
    projekcije.append({"id": len(projekcije), "datum": datum, "vreme": vreme, "duzina": duzina, "film": film["ime"], "obrisana": False, "broj_slobodnih_mesta": broj_slobodnih_mesta, "broj_ukupnih_mesta": broj_ukupnih_mesta})
    for projekcija in projekcije:
        print("""
Datum: {0}
Vreme: {1}
Duzina: {2}
Film: {3}
Broj ukupnih mesta: {4}
Broj slobodnih mesta: {5}

""".format(projekcija["datum"], projekcija["vreme"], projekcija["duzina"], projekcija["film"], projekcija["broj_ukupnih_mesta"], projekcija["broj_slobodnih_mesta"]))

def pretraga_projekcija():
    print("Ova opcija nije omogucena.")
    
def brisanje_projekcije():
    print("Ova opcija nije omogucena.")

def izmena_projekcije():
    print("Ova opcija nije omogucena.")    
    

