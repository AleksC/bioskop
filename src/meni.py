
nepostojeca_opcija = "Odabrana nepostojeca opcija! Molimo odaberite neku od ponudjenih opcija."
nepostojeca_funkcija = "Ova opcija nije omogucena."

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
                    print(nepostojeca_funkcija)
                elif izbor == 2:
                    unos_projekcije()
                elif izbor == 3:
                    print(nepostojeca_funkcija)
                elif izbor == 4:
                    print(nepostojeca_funkcija)
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
                    user.login()
                elif izbor == 1:
                    print(nepostojeca_funkcija)
                elif izbor == 2:
                    print(nepostojeca_funkcija)
                else:
                    print(nepostojeca_opcija)
            except ValueError:
                print(nepostojeca_opcija)

