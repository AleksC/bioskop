import json
import datetime
from provere import unos_broja
from rad_sa_fajlovima import ucitavanje_podataka
from filmovi import unos_filma, izbor_zanra

sale = ucitavanje_podataka("../data/sale.json")
projekcije = ucitavanje_podataka("../data/projekcije.json")

def unos_datuma():
    '''
    Funkcija koja proverava da li je datum unesen u ispravnom formatu
    i proverava da li unesen datum u buducem vremenu.
    '''
    danasnji_datum = datetime.date.today()
    while True:
        try:
            uneti_datum = input("Unesite datum projkecije u formatu dd mm yyyy: ")
            uneti_datum = datetime.datetime.strptime(uneti_datum, "%d %m %Y").date()
            if uneti_datum < danasnji_datum:
                print("Molimo unesite datum koji je u buducnosti.")
            else:
                break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return uneti_datum        

def unos_vremena(): 
    '''
    Funkcija koja proverava da li je vreme uneseno u ispravnom formatu.
    '''
    while True:
        try:
            vreme = input("Unesite vreme projkecije u formatu hh mm: ")
            vreme = datetime.datetime.strptime(vreme, "%H %M").time()
            break
        except ValueError:
            print("Molimo unesite podatke u navedenom formatu.")
    return vreme

def izbor_sale(): 
    '''
    Funkcija za odabir sale.
    Vraca odabranu salu, kao i sve njene vrednosti,
    kao sto su broj slobodnih i ukupnih mesta.
    '''
    while True:
        try:
            for i in range(len(sale)):
                print(str(i + 1) + " - " + sale[i]["ime_sale"])
            izbor = int(input("Vas izbor: "))
            return sale[izbor - 1]
        except ValueError:
            print("Molimo unesite broj ispred imena sale.")
        except IndexError:
            print("Izabrali ste nepostojecu salu. Molimo da odaberete neki od ponudjenih.")
            
def izbor_filma():
    '''
    Funkcija ucitava i ispisuje sve filmove.
    Nudi mogucnost dodavanja novog filma.
    '''
    print("Izaberite jedan od ponudjenih filmova: ")
    izbor = None
    while True:
        filmovi = ucitavanje_podataka("../data/filmovi.json")
        for i in range(len(filmovi)):
            print(str(i + 1) + " - " + filmovi[i]["ime"] + " | " + filmovi[i]["zanr"] + " | Trajanje: " + filmovi[i]["duzina"]+ " minuta.")
        print(str(i + 2) + " - Unos novog filma")
        try:
            izbor = int(input("Vas izbor: "))
            izbor = filmovi[izbor-1]
            break
        except ValueError:
            print("Molimo unesite broj ispred imena zeljenog filma.")
        except IndexError:
            if izbor == len(filmovi)+1:
                unos_filma()
            else:
                print("Izabrali ste nepostojeci film. Ukoliko zelite da dodate novi film pritisnite " + str(len(filmovi)+1))
    return izbor

def provera_poklapanja_projekcija(datum, vreme, sala, duzina):
    '''
    Proverava da li je uneta projekcija u konfliktu sa postojecom po pitanju datuma i sale.
    Zatim proverava da li se pocetak unete projekcije desava za vreme trajanje postojece,
    kao i da li se kraj unete projekcije desava u vreme kada je vec postojeca projekcija u toku.
    '''
    vreme_unete_projekcije = vreme.split()
    pocetak_unete_projekcije = datetime.timedelta(hours = int(vreme_unete_projekcije[0]), minutes = int(vreme_unete_projekcije[1]))
    kraj_unete_projekcije = pocetak_unete_projekcije + datetime.timedelta(minutes = int(duzina))
    for i in projekcije:
        if sala == i["sala"] and datum == i["datum"]:
            vreme_postojece_projekcije = i["vreme"].split()
            pocetak_postojece_projekcije = datetime.timedelta(hours = int(vreme_postojece_projekcije[0]), minutes = int(vreme_postojece_projekcije[1]))
            kraj_postojece_projekcije =  pocetak_postojece_projekcije + datetime.timedelta(minutes = int(i["duzina"]))
            if pocetak_unete_projekcije >= pocetak_postojece_projekcije and pocetak_unete_projekcije <= kraj_postojece_projekcije:
                return True
            elif pocetak_postojece_projekcije >= pocetak_unete_projekcije and pocetak_postojece_projekcije <= kraj_unete_projekcije:
                return True
    return False

def unos_projekcije():
    '''
    Nakon svih potrebnih provera unosa, upisuje projekciju u vec postojecu listu projekcija.
    Stampa korisniku unetu projekciju.
    '''
    print("Unos nove projekcije: ")
    identifikator = str(len(projekcije)+1)
    film = izbor_filma()
    duzina = str(film["duzina"])
    while True:
        datum = unos_datuma().strftime("%d %m %Y")
        vreme = unos_vremena().strftime("%H %M")
        print("Izaberite salu u kojoj ce se odrzavati projekcija: ")
        sala = izbor_sale()
        if provera_poklapanja_projekcija(datum, vreme, sala["ime_sale"], int(duzina)):
            print("Molimo unesite projekciju u drugom terminu ili drugoj sali.")
        else:
            break   
    cena = str(unos_broja("Molimo unesite cenu projekcije u dinarima: "))
    broj_slobodnih_mesta = str(sala["kapacitet"])
    broj_ukupnih_mesta = str(sala["kapacitet"])
    uneta_projekcija = {"id": identifikator, "datum": datum, "vreme": vreme, "duzina": duzina, "cena": cena, "film": film["ime"], "zanr": film["zanr"], "sala": sala["ime_sale"], "obrisana": "False", "broj_slobodnih_mesta": broj_slobodnih_mesta, "broj_ukupnih_mesta": broj_ukupnih_mesta}
    
    with open('../data/projekcije.json', 'w') as fajl:
        projekcije.append(projekcije.append(uneta_projekcija))
        projekcije.pop()
        json.dump(projekcije, fajl)

    id_unete_projekcije = int(uneta_projekcija["id"])-1
    print("""
Uneli ste projekciju:
Datum: {datum}
Vreme: {vreme}
Duzina: {duzina}
Film: {film}
Zanr: {zanr}
Sala: {sala}
Cena: {cena}
Broj ukupnih mesta: {broj_ukupnih_mesta}
Broj slobodnih mesta: {broj_slobodnih_mesta} 
""".format(**projekcije[id_unete_projekcije]))

def pretraga_projekcija(): 
    '''
    Fine tuning required.
    Koment na gornji koment. 
    Fine tuning cega? Retarde.
    '''
    while True:
        print("Pretrazite projekciju prema:")
        print("1 - ID-u projekcije")
        print("2 - Nazivu filma")
        print("3 - Zanru filma")
        print("4 - Sali prikazivanja")
        print("0 - Povratak na prethodni meni")
        unos = unos_broja()
        if unos == 0:
            break
        elif unos == 1:
            prikazanih_projekcija = 0
            print("Molimo unesite zeljeni ID projekcije.")
            unos_id = unos_broja()
            for i in projekcije:
                if str(unos_id) == i["id"]:
                    print(i["film"] + " | " + str(i["datum"]) + " u " + str(i["vreme"]))
                    prikazanih_projekcija += 1
            if prikazanih_projekcija == 0:
                print("Ne postoji projekcija za datim ID-om.")
        elif unos == 2:
            prikazanih_projekcija = 0
            naziv_filma = input("Molimo unesite zeljeni naziv filma: ")
            naziv_filma_odvojeno = naziv_filma.split()
            for i in projekcije:
                if naziv_filma.lower() == i["film"].lower():
                    print(i["film"] + " | " + str(i["datum"]) + " u " + str(i["vreme"]))
                    prikazanih_projekcija += 1
                else:
                    for j in naziv_filma_odvojeno:
                        if j in i["film"].lower().split():
                            print(i["film"] + " | " + str(i["datum"]) + " u " + str(i["vreme"]))
                            prikazanih_projekcija += 1
            if prikazanih_projekcija == 0:
                print("Ne postoji projekcija za unetim imenom.")
        elif unos == 3:
            zanr_filma = izbor_zanra()
            prikazanih_projekcija = 0
            for i in projekcije:
                if zanr_filma.lower() == i["zanr"].lower():
                    print(i["film"] + " | " + str(i["datum"]) + " u " + str(i["vreme"]))
                    prikazanih_projekcija += 1
            if prikazanih_projekcija == 0:
                print("Nema filmova u ovom zanru.")
        elif unos == 4:
            sala_prikazivanja = izbor_sale()
            prikazanih_projekcija = 0
            for i in projekcije:
                if sala_prikazivanja["ime_sale"].lower() == i["sala"].lower():
                    print(i["film"] + " | " + str(i["datum"]) + " u " + str(i["vreme"]))
                    prikazanih_projekcija += 1
            if prikazanih_projekcija == 0:
                print("Izabrali ste nepostojecu salu.")

def brisanje_projekcije(): 
    '''
    Funkcija za brisanje projekcija.
    Pretrazuje projekcije koje nisu vec obrisane i brise onu koju je korisnik odabrao.
    '''
    print("Odaberite projekciju za brisanje:")
    projekcije = ucitavanje_podataka("../data/projekcije.json")
    projekcija_obrisana = False
    while not projekcija_obrisana:
        for projekcija in projekcije:
            if projekcija["obrisana"] == "False":
                print(str(projekcija["id"]) + " - " + projekcija["film"] + " | " + str(projekcija["datum"]) + " u " + str(projekcija["vreme"]))
        print("0 - Povratak na prethodni meni.")
        unos = unos_broja()
        if unos == 0:
            break
        for projekcija in projekcije:
            if unos == int(projekcija["id"]):
                if projekcije[unos-1]["obrisana"] == "False":
                    with open('../data/projekcije.json', 'w') as fajl:
                        projekcije[unos-1]["obrisana"] = "True"
                        json.dump(projekcije, fajl)
                    projekcija_obrisana = True
        if not projekcija_obrisana:
            print("Molimo unesite ispravan unos.")


def izmena_projekcije(): 
    '''
    Funkcija za brisanje projekcije. 
    Posle svake promene vrsi se provera da li je posle promene projekcija i dalje validna.
    '''
    while True:
        print("Odaberite projekciju za izmenu odabirom id-ja projekcije.")
        for i in projekcije:
            print("{id} | {film} | {datum} | {vreme} | {sala}".format(**i) )
        print("0 - Povratak na prethodni meni")
        izbor = None
        while True:
            try:   
                unos = unos_broja()-1
                if unos == -1:
                    izbor = unos
                    break
                projekcija = projekcije[unos]
                izbor = unos
                break
            except IndexError:
                print("Molimo unesite jednu od ponudjenih opcija.")
        if izbor == -1:
            break
        print("Odaberite sta zelite da menjate u vezi izabrane projekcije.")
        print("1 - Datum: " + projekcija["datum"])
        print("2 - Vreme: " + projekcija["vreme"])
        print("3 - Sala: " + projekcija["sala"])
        print("4 - Cena: " + projekcija["cena"])
        print("0 - Povratak na prethodni meni")
        unos = unos_broja()
        while True:
            if unos == 1:
                while True:
                    promenjen_datum = unos_datuma().strftime("%d %m %Y")
                    if provera_poklapanja_projekcija(promenjen_datum, projekcija["vreme"], projekcija["sala"], projekcija["duzina"]):
                        print("Molimo unesite projekciju u drugom terminu ili drugoj sali.")
                    else:
                        with open('../data/projekcije.json', 'w') as fajl:
                            projekcije[izbor]["datum"] = promenjen_datum
                            json.dump(projekcije, fajl) 
                        break
                break
            elif unos == 2:
                while True:
                    promenjeno_vreme = unos_vremena().strftime("%H %M")
                    if provera_poklapanja_projekcija(projekcija["datum"], promenjeno_vreme, projekcija["sala"], projekcija["duzina"]):
                        print("Molimo unesite projekciju u drugom terminu ili drugoj sali.")
                    else:
                        with open('../data/projekcije.json', 'w') as fajl:
                            projekcije[izbor]["vreme"] = promenjeno_vreme
                            json.dump(projekcije, fajl) 
                        break
                break
            elif unos == 3:
                while True:
                    promenjena_sala = izbor_sale()
                    if provera_poklapanja_projekcija(projekcija["datum"], projekcija["vreme"], promenjena_sala, projekcija["duzina"]):
                        print("Molimo unesite projekciju u drugom terminu ili drugoj sali.")
                    else:
                        with open('../data/projekcije.json', 'w') as fajl:
                            projekcije[izbor]["sala"] = promenjena_sala["sala"]
                            json.dump(projekcije, fajl) 
                        break
                break
            elif unos == 4:
                with open('../data/projekcije.json', 'w') as fajl:
                    projekcije[izbor]["cena"] = unos_broja("Molimo unesite novu cenu projekcije: ")
                    json.dump(projekcije, fajl) 
                break
