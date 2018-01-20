import json
import provere as p
from rad_sa_fajlovima import ucitavanje_podataka


def login(korisnici): 
    '''
    Funkcija za login. Trazi kao argument podatke o svim korisnicima u bazi
    i proverava da li se uneseno korisnicko ime i sifra poklapaju sa podacima iz baze.
    Vraca odgovarajuceg korisnika.
    '''
    while True:
        print("Unesite podatke za logovanje na sistem:")
        korisnicko_ime = input("Korisnicko ime: ") 
        sifra = input("Sifra: ") 
        for korisnik in korisnici: 
            if korisnicko_ime == korisnik["korisnicko_ime"] and sifra == korisnik["sifra"]: 
                print("Ulogovani ste kao {ime} {prezime}".format(**korisnik))    
                return korisnik
            elif korisnicko_ime == "" or sifra == "":
                print("Korisnicko ime i/ili lozinka ne mogu biti prazni!")
                break
        print("Korisnicko ime i/ili lozinka nisu pronadjeni!") 

def dodavanje_korisnika():
    '''
    Funkcija pomocu koje menadzer dodaje novog prodavca ili menadzera.
    Podaci se ucitavaju, na njih se dodaje novi korisnik, zatim se upisuje u json fajl.
    '''
    korisnici = ucitavanje_podataka("../data/korisnici.json")
    ime = p.unos_stringa("ime")
    prezime = p.unos_stringa("prezime")
    korisnicko_ime = p.provera_poklapanja("korisnicko_ime", "Molimo unesite korisnicko ime novog korisnika: ", korisnici)
    sifra = input("Molimo unesite sifru novog korisnika: ")
    while True:
        try:
            uloga = p.unos_broja("""Molimo oznacite ulogu novog korisnika odabirom odgovarajuceg rednog broja: 
0 - menadzer
1 - prodavac
Vas izbor: """)
            if uloga == 0:
                uloga = "menadzer"
                break
            elif uloga == 1:
                uloga = "prodavac"
                break
            else:
                print("Molimo odaberite neku od ponudjenih opcija.")
        except ValueError:
            print("Odabrana nepostojeca opcija! Molimo odaberite neku od ponudjenih opcija.")
    novi_korisnik = {"ime": ime, "prezime": prezime, "korisnicko_ime": korisnicko_ime, "sifra": sifra, "uloga": uloga}

    while True:
        print("Da li ste sigurni da zelite da dodate novog prodavca {ime} {prezime}".format(**novi_korisnik))
        print("1 - Da")
        print("0 - Ne (Povratak na prethodni meni)")
        izbor = p.unos_broja()
        if izbor == 1:
            with open('../data/korisnici.json', 'w') as fajl:
                korisnici.append(novi_korisnik)
                json.dump(korisnici, fajl)
                print("Korisnik uspesno dodat!")
            break
        elif izbor == 0:
            print("Unos korisnika otkazan!")
            break
        
        
                

