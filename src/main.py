from korisnik import login
from projekcije import *
from racun import racun

nepostojeca_opcija = "Odabrana nepostojeca opcija! Molimo odaberite neku od ponudjenih opcija."

def main():
    while True:
        glavni_meni(login())

def glavni_meni(korisnik): #funkcija za prikaz menija
    if korisnik["uloga"] == "menadzer": #prikaz menija za menadzera
        while True: #beskonacna petlja da se meni stalno prikazuje osim u slucaju odabira opcije log out
            print("0 - Log out")
            print("1 - Pretraga projekcija")
            print("2 - Unos nove projekcije")
            print("3 - Brisanje projekcije")
            print("4 - Izmena projekcije")
            try:
                izbor = int(input("Odaberite opciju: ")) #odabir opcije i poziv odgovarajuce funkcije
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
                    print(nepostojeca_opcija) #slucaj da je korisnik odabrao nepostojecu opciju
            except ValueError: #exception u slucaju da korisnik ne unese broj
                print(nepostojeca_opcija)

    else: #prikaz menija za prodavca
        while True: #beskonacna petlja da se meni stalno prikazuje osim u slucaju odabira opcije log out
            print("0 - Log out")
            print("1 - Pretraga projekcija")
            print("2 - Prodaja karata")
            try:
                izbor = int(input("Odaberite opciju: ")) #odabir opcije i poziv odgovarajuce funkcije
                if izbor == 0:
                    break
                elif izbor == 1:
                    pretraga_projekcija()
                elif izbor == 2:
                    racun()
                else:
                    print(nepostojeca_opcija) #slucaj da je korisnik odabrao nepostojecu opciju
            except ValueError: #exception u slucaju da korisnik ne unese broj
                print(nepostojeca_opcija)
                
if __name__ == "__main__":
    main()
