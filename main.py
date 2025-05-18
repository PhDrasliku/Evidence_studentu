from spravce_studentu import SpravceStudentu
from pomocne_fukce import validuj_male_cislo, zadej_cislo, vycisti_obrazovku, validuj_text, validuj_telefon
from Student import Student

def menu():
    print("*" * 28)
    print("    EVIDENCE STUDENTŮ")
    print("*" * 28)
    print("1 - Přidat nového studenta")
    print("2 - Vypsat všechny studenty")
    print("3 - Vyhledat studenta")
    print("4 - Smazání studenta dle ID")
    print("5 - Konec")
    print("-" * 28)
    print("11 - Generace studenta")
    print("12 - Reset databáze")
    print("-" * 28)

pokracovat = ""
spravce = SpravceStudentu()
while pokracovat != "a":
    menu()
    volba = input("Zadejte číslo akce: ")
    if volba == "1":
        try:
            jmeno = validuj_text("Zadejte JMÉNO studenta: ")
            prijmeni = validuj_text("Zadejte PŘÍJMENÍ: ")
            telefon = validuj_telefon("Zadejte TELEFONNÍ ČÍSLO: ")
            vek = zadej_cislo("Zadejte VĚK: ")
            spravce.pridej_studenta(jmeno, prijmeni, vek, telefon)
            input("Data byla uložena. Pokračuj libovolnou klávesou...")
        except ValueError as e:
            print(f"Chyba: {e}")
            input("Pokračuj libovolnou klávesou...")

    elif volba == "2":
        Student.hlavicka()
        print(spravce.zobraz_vsechny())
        input("Pokračujte libovolnou klávesou...")

    elif volba == "3":            
        print("Můžete zadat pouze jméno, pouze příjmení, nebo obojí.")
        jmeno = input("Zadejte JMÉNO studenta (nepovinné): ")
        prijmeni = input("Zadejte PŘÍJMENÍ studenta (nepovinné): ")
        Student.hlavicka()
        print(spravce.vyhledej_studenta(jmeno, prijmeni))
        input("Pokračujte libovolnou klávesou...")

    elif volba == "4":
        id = (input("Zadejte ID studenta ke smazání: "))
        print(spravce.odstran_studenta(id))
        input("Pokračuj libovolnou klávesou...")

    elif volba == "11":
        pocet = validuj_male_cislo(input("Bude vytvořen 1 student nebo zadej kolik studentů bude vygenerováno 1-10: "))
        for _ in range(pocet):
            print(spravce.generuj_studenta())
        input("Data byla uložena. Pokračuj libovolnou klávesou...")

    elif volba == "12":
        potv = input("Opravdu chcete vymazat všechny studenty? [A/N]: ")
        if potv.strip().lower() == "a":
            reset_id = input("Chcete resetovat i čítač ID? (začne opět od 1) [A/N]: ")
            spravce.reset_databaze(reset_id.strip().lower() == "a")
            print("Databáze byla vymazána.")
            input("Pokračujte libovolnou klávesou...")

    elif volba == "5":
        potv = input("Aplikace bude ukončena a data uložena. Přejete si pokračovat? [A/N]: ")
        if potv.strip().lower() == "a":
            spravce.uloz_data()
            pokracovat = "a"
    vycisti_obrazovku()