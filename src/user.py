import meni

petar = {"korisnickoIme": "Petar123",
         "sifra": "123",
         "ime": "Petar",
         "prezime": "Petrovic",
         "uloga": "menadzer"
         }

milan = {"korisnickoIme": "Milan123",
         "sifra": "123",
         "ime": "Milan",
         "prezime": "Milanovic",
         "uloga": "prodavac"
         }

korisnici = {"korisnik": petar,
             "korisnik": milan}


def login():
    print("Unesite podatke za logovanje na sistem:")
    username = input("Korisnicko ime: ")
    password = input("Sifra: ")
    if username in korisnici["korisnik"]["korisnickoIme"] and password in korisnici["korisnik"]["sifra"]:
        print("Ulogovani ste kao {0} {1}".format(korisnici["korisnik"]["ime"], korisnici["korisnik"]["prezime"]))    
        if "menadzer" in korisnici["korisnik"]["uloga"]:
            meni.glavniMeni("menadzer")
        elif "prodavac" in korisnici["korisnik"]["uloga"]:
            meni.glavniMeni("prodavac")
            
    elif username == "" or password == "":
          print("Korisnicko ime i/ili lozinka ne mogu biti prazni!")
          login()
    else:
          print("Korisnicko ime i/ili lozinka nisu pronadjeni!")
          login()


        


