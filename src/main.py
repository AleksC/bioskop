from korisnik import login, dodavanje_korisnika
from projekcije import pretraga_projekcija, unos_projekcije, brisanje_projekcije, izmena_projekcije
from racun import racun
from rad_sa_fajlovima import ucitavanje_podataka

nepostojeca_opcija = "Odabrana nepostojeca opcija! Molimo odaberite neku od ponudjenih opcija."

def main():
    """
    Podaci se ucitavaju svakim ulaskom u meni u slucaju promene podataka ponudjenim opcijama u meniju.
    """
    while True:
        ucitavanje_korisnika = ucitavanje_podataka("../data/korisnici.json")
        ulogovan_korisnik = login(ucitavanje_korisnika)
        glavni_meni(ulogovan_korisnik)

def glavni_meni(korisnik):
    '''
    Beskonacna petlja postoji da bi se meni stalno prikazivao.
    Odogovarajuci meni se prikazuje prema unetom argumentu.
    '''
    if korisnik["uloga"] == "menadzer": 
        while True: 
            print("0 - Log out")
            print("1 - Pretraga projekcija")
            print("2 - Unos nove projekcije")
            print("3 - Brisanje projekcije")
            print("4 - Izmena projekcije")
            print("5 - Dodavanje novog korisnika")
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
                elif izbor == 5:
                    dodavanje_korisnika()
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
                
if __name__ == "__main__":
    main()
