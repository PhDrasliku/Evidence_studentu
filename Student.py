class Student:
    id = 0
    def __init__(self, jmeno, prijmeni, vek, telefon, id=None):
        if id is not None:
            self.id = id
        else:
            Student.id += 1
            self.id = Student.id
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def to_dict(self):
        return {
            "jmeno": self.jmeno,
            "prijmeni": self.prijmeni,
            "vek": self.vek,
            "telefon": self.telefon,
            "id": self.id
        }

    def __str__(self):
        return f"{self.id:<3} | {self.jmeno:<12} | {self.prijmeni:<14} | {self.vek:<5} | {self.telefon:<15}"
    
    @staticmethod
    def hlavicka():
        print("ID  |    Jméno     |    Příjmení    |  Věk  | Telefonní číslo   ")

    @staticmethod
    def from_dict(data):
        return Student(
            data["jmeno"],
            data["prijmeni"],
            data["vek"],
            data["telefon"],
            data.get("id")
        )