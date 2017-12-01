from korisnik import login
from projekcije import *
from racun import racun

nepostojeca_opcija = "Odabrana nepostojeca opcija! Molimo odaberite neku od ponudjenih opcija."

def main():
    while True:
        glavni_meni(login())

def glavni_meni(korisnik):
    if korisnik["uloga"] == "menadzer": 
        while True:
            print("0 - Log out")
            print("1 - Pretraga projekcija")
            print("2 - Unos nove projekcije")
            print("3 - Brisanje projekcije")
            print("4 - Izmena projekcije")
            try:
                izbor = int(input("Odaberite opciju: "))
                if izbor == 0:
                    break
                elif izbor == 1:
                    pretraga_projekcija()
                elif izbor == 2:
                    unos_projekcije()
                elif izbor == 3:
                    brisanje_projekcije()
                elif izbor == 4:
                    izmena_projekcije()
                else:
                    print(nepostojeca_opcija)
            except ValueError:
                print(nepostojeca_opcija)

    else:
        while True:
            print("0 - Log out")
            print("1 - Pretraga projekcija")
            print("2 - Prodaja karata")
            try:
                izbor = int(input("Odaberite opciju: "))
                if izbor == 0:
                    break
                elif izbor == 1:
                    pretraga_projekcija()
                elif izbor == 2:
                    racun()
                else:
                    print(nepostojeca_opcija)
            except ValueError:
                print(nepostojeca_opcija)
                

main()
