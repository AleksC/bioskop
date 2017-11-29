korisnici = [{"korisnicko_ime": "Petar123",
             "sifra": "123",
             "ime": "Petar",
             "prezime": "Petrovic",
             "uloga": "menadzer"
             },
             {"korisnicko_ime": "Milan123",
             "sifra": "123",
             "ime": "Milan",
             "prezime": "Milanovic",
             "uloga": "prodavac"
             }
             ]

def login(): #funkcija za login
    while True:
        print("Unesite podatke za logovanje na sistem:")
        username = input("Korisnicko ime: ") #unos podataka
        password = input("Sifra: ") #unos podataka
        for korisnik in korisnici: #prolazak kroz listu svih korisnika
            if username == korisnik["korisnicko_ime"] and password == korisnik["sifra"]: #proveravanje postojanja korisnika u bazi podataka
                print("Ulogovani ste kao {0} {1}".format(korisnik["ime"], korisnik["prezime"]))    
                return korisnik
            elif username == "" or password == "": #slucaj da korisnik slucajno ili namerno ne unese nijedan podatak
                print("Korisnicko ime i/ili lozinka ne mogu biti prazni!")
                break
        else:
            print("Korisnicko ime i/ili lozinka nisu pronadjeni!")


