import os
import unicodedata    

chybne_pokusy = 3


def zadej_cislo(kontrolovany_vek):       
    """
    Funkce pro validaci věku.
    Kontroluje, zda je věk v rozmezí 6-35 let.
    Pokud je věk neplatný, zobrazí chybovou hlášku a požádá o nový vstup.
    povoluje maximálně pokusy dle proměné "Chybné_pokusy".
    :param kontrolovany_vek: číselný vstup pro věk.
    :return: Platný věk v rozmezí 6-35 let.
    """
    pokusy = 0
    while pokusy < chybne_pokusy:  
        try:
            vek = int(input(kontrolovany_vek))
            if 6 <= vek <= 35:
                return vek
            print("Osoba se ještě moc mladá na studium nebo to fakt nemůže být student (ověř si věk)") 
        except ValueError:
            print("Zadejte prosím věk od 6 do 35 let.")
        pokusy += 1
    raise ValueError("Překročen maximální počet pokusů.")
                
def vycisti_obrazovku():
    """
    Funkce pro vyčištění obrazovky (funkční pouze na windows). 
    """
    os.system('cls')

def validuj_text(text):
    """
    Funkce pro validaci Jména a přímení vstupu.
    Kontroluje, zda je vstupní text neprázdný a zda obsahuje pouze písmena.
    Pokud je vstup prázdný nebo obsahuje jiné znaky, zobrazí chybovou hlášku a požádá o nový vstup.
    Pokud uživatel zadá 2x posobě stejný neplatný vstup, akceptuje ho jako platný vstup (pokud není prázdný).
    povoluje maximálně pokusy dle proměné "Chybné_pokusy".
    :param text: Text, který se má validovat.
    :return: Platný vstupní text.
    """
    posledni_pokus = None
    pokusy = 0
    while pokusy < chybne_pokusy:  
        vstup = input(text).strip()
        if vstup and vstup.isalpha() and 3 <= len(vstup) <= 12:
            return vstup
        elif vstup == posledni_pokus and vstup != "":
            print(f"Hodnota {vstup} byla přijata")
            posledni_pokus = None
            return vstup
        else:
            posledni_pokus = vstup
            print("hodnota musí mít 3 až 12 PÍSMEN! Pro vyjímku zadej stejnou hodnotu znovu, hodnota nesmí byt prázdná")
        pokusy += 1
    raise ValueError("Překročen maximální počet pokusů.")

def validuj_telefon(tel):
    """
    Funkce pro validaci telefonního čísla.
    Kontroluje, zda je telefonní číslo ve správném formátu.
    Pokud je číslo platné, vrátí ho ve formátu "+420 123 456 789" nebo "123 456 789".
    :param tel: 9 číslic, připadně začínající "+".
    :return: Platné telefonní číslo ve formátu předvolba +1/+12/+123 nasledovaných 9 čísly ve formátu "123 456 789".
    """
    pokusy = 0
    while pokusy < chybne_pokusy:  
        telefon = input(tel)
        cislo = telefon.replace(" ", "")
        
        if cislo.startswith("+"):
            predvolba = ""
            zbytek = ""
            
            for i in range(1, 4):
                predvolba = cislo[0:1+i]
                zbytek = cislo[1+i:]
            
                if len(zbytek) == 9 and zbytek.isdigit():
                    return f"{predvolba} {zbytek[0:3]} {zbytek[3:6]} {zbytek[6:]}"
            print("Neplatná předvlba")
            continue  # zabrání vypsání další hlášky
        else:
            if len(cislo) == 9 and cislo.isdigit():
                return f"{cislo[0:3]} {cislo[3:6]} {cislo[6:]}"
        print("Neplatné číslo")
        pokusy += 1
    raise ValueError("Překročen maximální počet pokusů.")       

def normalize(text):
    """
    Funkce pro normalizaci textu.
    Odstraňuje diakritiku a převádí text na malá písmena.
    :param text: Text, který se má normalizovat.
    :return: Normalizovaný text bez diakritiky a převedený na malá písmena.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def validuj_male_cislo(cislo):
    """
    Funkce pro validaci malého čísla v rozmezí 1-10.
    Pokud je hodnota mimo rozsah nebo neplatné, vrátí výchozí hodnotu 1.
    :param cislo: Číslo, které se má validovat.
    :return: Platné číslo v rozmezí 1-10 nebo výchozí hodnota 1.
    """

    vstup = cislo.strip()
    try:
        vstup = int(vstup)
        if  0 < vstup <= 10:
            return vstup
        vstup = 1
        return vstup
    except ValueError:
        vstup = 1
        return vstup
        