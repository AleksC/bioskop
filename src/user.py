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

korisnici = [petar, milan]

def login():
    print("Unesite podatke za logovanje na sistem:")
    username = input("Korisnicko ime: ")
    password = input("Sifra: ")
    for i in range(len(korisnici)):
        if username in korisnici[i]["korisnickoIme"] and password in korisnici[i]["sifra"]:
            print("Ulogovani ste kao {0} {1}".format(korisnici[i]["ime"], korisnici[i]["prezime"]))    
            if "menadzer" in korisnici[i]["uloga"]:
                meni.glavniMeni("menadzer")
            elif "prodavac" in korisnici[i]["uloga"]:
                meni.glavniMeni("prodavac")
            
            elif username == "" or password == "":
                  print("Korisnicko ime i/ili lozinka ne mogu biti prazni!")
                  login()
    else:
          print("Korisnicko ime i/ili lozinka nisu pronadjeni!")
          login()


        


