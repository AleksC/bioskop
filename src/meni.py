import main

def glavniMeni(uloga):
    if uloga == "menadzer":
        print("0 - Log out")
        print("1 - Pretraga projekcija")
        print("2 - Unos nove projekcije")
        print("3 - Brisanje projekcije")
        print("4 - Izmena projekcije")
        izbor = int(input("Odaberite opciju: "))
        if izbor == 0:
            main.user.login()
        elif izbor == 1:
            main.projekcije.pretragaProjekcija()
        elif izbor == 2:
            main.projekcije.unosProjekcije()
            return glavniMeni("menadzer")
        elif izbor == 3:
            main.projekcije.brisanjeProjekcije()
            glavniMeni("menadzer")
        elif izbor == 4:
            projekcije.izmenaProjekcije()
        else:
            print("Odabrana nepostojeca opcija! Molimo odaberite neke od narednih opcija")
            return glavniMeni("menadzer")
            
    elif uloga == "prodavac":
        print("0 - Log out")
        print("1 - Pretraga projekcija")
        print("2 - Prodaja karata")
        izbor = int(input("Odaberite opciju: "))
        if izbor == 0:
            main.user.login()
        elif izbor == 1:
            main.projekcije.pretragaProjekcija()
        elif izbor == 2:
            prodajaKarata()
        else:
            print("Odabrana nepostojeca opcija! Molimo odaberite neke od narednih opcija")
            glavniMeni("prodavac")

        

