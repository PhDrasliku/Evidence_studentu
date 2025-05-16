from Student import Student
import random
from pomocne_fukce import normalize
import json

class SpravceStudentu:
    def __init__(self):
        self.studenti = []
        self.nacti_data()

    def pridej_studenta(self, jmeno, prijmeni, vek, telefon):
        novy = Student(jmeno, prijmeni, vek, telefon)
        self.studenti.append(novy)

    def zobraz_vsechny(self):
        if not self.studenti:
            return "Žádní studenti nejsou evidováni."
        return "\n".join(str(s) for s in self.studenti)


    def vyhledej_studenta(self, jmeno, prijmeni):
        """
        Vyhledá studenta podle jména a/nebo příjmení.
        Může být zadáno pouze jméno, pouze příjmení nebo obojí.
        :param jmeno: Jméno studenta (nepovinné).
        :param prijmeni: Příjmení studenta (nepovinné).
        :return: Seznam nalezených studentů nebo zpráva o nenalezení.
        """
        nalezeni = []
        jmeno = normalize(jmeno.strip()) if jmeno.strip() else ""
        prijmeni = normalize(prijmeni.strip()) if prijmeni.strip() else ""

        for s in self.studenti:
            normalized_jmeno = normalize(s.jmeno)
            normalized_prijmeni = normalize(s.prijmeni)

            jmeno_ok = jmeno in normalized_jmeno if jmeno else True
            prijmeni_ok = prijmeni in normalized_prijmeni if prijmeni else True

            if jmeno_ok and prijmeni_ok:
                nalezeni.append(s)

        if not nalezeni:
            return "Student nebyl nalezen."
        return "\n".join(str(s) for s in nalezeni)


    def odstran_studenta(self, id):
        for s in self.studenti:
            if str(s.id) == (id):
                self.studenti.remove(s)
                return f"Student s ID: '{id}' byl úspěšně odstraněn."
        return f"Student s ID {id} nebyl nalezen."



    def generuj_studenta(self):
        jmena = ["Jan", "Petr", "Jakub", "Martin", "Pepek", "Prokop",]
        prijmeni = ["Novák", "Čech", "Dvořák", "Černý", "Čermák", "Kny"]

        jmeno = random.choice(jmena)
        prijmeni = random.choice(prijmeni)
        vek = random.randint(18, 35)
        random_telefon = str(random.randint(0, 999_999_999)).zfill(9)
        telefon = f"{random_telefon[:3]} {random_telefon[3:6]} {random_telefon[6:]}"

        self.pridej_studenta(jmeno, prijmeni, vek, telefon)
        return f"Náhodný student {jmeno} {prijmeni}, {vek} let, tel.:{telefon} byl přidán."


    # Uložení dat do JSON souboru

    def uloz_data(self, soubor="studenti.json"):
        with open(soubor, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.studenti], f, ensure_ascii=False, indent=2)

    def nacti_data(self, soubor="studenti.json"):
        try:
            with open(soubor, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.studenti = [Student.from_dict(s) for s in data]
                if self.studenti:
                    max_id = max(s.id for s in self.studenti)
                    Student.id = max_id
                else:
                    Student.id = 0
        except (FileNotFoundError, json.JSONDecodeError):
            self.studenti = []
            Student.id = 0

    def reset_databaze(self, reset_id=False, soubor="studenti.json"):
        self.studenti = []
        if reset_id:
            Student.id = 0
        self.uloz_data(soubor)
