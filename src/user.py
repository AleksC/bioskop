import main

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

korisnici = [petar, milan]

def login():
    print("Unesite podatke za logovanje na sistem:")
    username = input("Korisnicko ime: ")
    password = input("Sifra: ")
    for i in range(0, len(korisnici)):
        if username == korisnici[i]["korisnickoIme"] and password == korisnici[i]["sifra"]:
            print("Ulogovani ste kao {0} {1}".format(korisnici[i]["ime"], korisnici[i]["prezime"]))    
            if "menadzer" == korisnici[i]["uloga"]:
                return main.meni.glavniMeni("menadzer")
            elif "prodavac" == korisnici[i]["uloga"]:
                return main.meni.glavniMeni("prodavac")
        elif username == "" or password == "":
            print("Korisnicko ime i/ili lozinka ne mogu biti prazni!")
            return login()
        elif i == (len(korisnici) - 1) and username != korisnici[i]["korisnickoIme"] or password != korisnici[i]["sifra"]:
            print("Korisnicko ime i/ili lozinka nisu pronadjeni!")
            return login()
        
    


login()


