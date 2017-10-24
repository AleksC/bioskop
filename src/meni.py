import user
import projekcije

def glavniMeni(uloga):
    if uloga == "menadzer":
        print("0 - Log out")
        print("1 - Pretraga projekcija")
        print("2 - Unos nove projekcije")
        print("3 - Brisanje projekcije")
        print("4 - Izmena projekcije")
        izbor = int(input("Odaberite opciju: "))
        if izbor == 0:
            user.login()
        elif izbor == 1:
            projekcije.pretragaProjekcija()
        elif izbor == 2:
            projekcije.unosProjekcije()
        elif izbor == 3:
            projekcije.brisanjeProjekcije()
        elif izbor == 4:
            projekcije.izmenaProjekcije()
        else:
            print("Odabrana nepostojeca opcija! Molimo odaberite neke od narednih opcija")
            glavniMeni("menadzer")
            
    elif uloga == "prodavac":
        print("0 - Log out")
        print("1 - Pretraga projekcija")
        print("2 - Prodaja karata")
        izbor = int(input("Odaberite opciju: "))
        if izbor == 0:
            user.login()
        elif izbor == 1:
            projekcije.pretragaProjekcija()
        elif izbor == 2:
            prodajaKarata()
        else:
            print("Odabrana nepostojeca opcija! Molimo odaberite neke od narednih opcija")
            glavniMeni("prodavac")

        

