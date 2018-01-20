def unos_stringa(ciljana_provera):
    '''
    Provera namenjena pravilnom unosu imena i prezimena novih korisnika.
    '''
    provera = False
    while not provera:
        string_za_proveru = input("Molimo unesite " + ciljana_provera + " novog korisnika: ")
        pom_prom = string_za_proveru.split()
        if len(pom_prom) != 1:
            print("Unesite samo " + ciljana_provera + ".")
            provera = False
            continue
        else:
            provera = True
        if not string_za_proveru.isalpha():
            print(ciljana_provera.capitalize() + " ne sme sadrzati brojeve.")
            provera = False
        else:
            provera = True

    return string_za_proveru

def unos_broja(tekst = "Vas izbor: "):
    '''
    Funkcija za proveru unosa broja.
    Uglavnom koriscena za navigaciju kroz menije.
    '''
    while True:
        try:
            unos = int(input(tekst))
            return unos
        except ValueError:
            print("Molimo unesite odgovarajuci broj.")


def provera_poklapanja(unos, tekst_za_unos, lokacija_pretrage):
    '''
    Funkcija za proveru postojanja unetog podatka u vec postojecim podacima.
    '''
    pom_prom = True
    while pom_prom:
        pretraga = input(tekst_za_unos)
        pom_prom = False
        for i in lokacija_pretrage:
            if pretraga in i[unos]:
                print(unos.capitalize().replace("_", " ") + " je nemoguce upotrebiti. Molimo pokusajte sa drugim unosom.")
                pom_prom = True
                break
    return pretraga


