class Student:
    def __init__(self, dzial, specjalizacja, semestr, klasa):
        self.dzial = dzial
        self.specjalizacja = specjalizacja
        self.semestr = semestr
        self.klasa = klasa

    def classs(self, name):
        return "Student o imieniu {} jest w grupie {}".format(name, self.klasa)

    def woot(self, name):
        return "Student o imieniu {} studiuje kierunek {} na specjalizacji {}".format(name, self.dzial, self.specjalizacja)

    def pain(self, name):
        if self.semestr < 2:
            return "Student o imieniu {} jest na {} semestrze".format(name, self.semestr)
        else:
            return "Student o imieniu {} jest już w {} semestrze".format(name, self.semestr)


student1 = Student("informatyka", "bazy danych", 1, "Grupa 3")
student2 = Student("Marketing", "Psychologia w marketingu", 3, "Grupa 1")
student3 = Student("Zamiatanie dywanów", "Psychologia dywanów", 7, "Grupa 10")

print(student1.classs("Mateusz"))
print(student1.woot("Mateusz"))
print(student1.pain("Mateusz"))

print(student2.classs("Stachu"))
print(student2.woot("Stachu"))
print(student2.pain("Stachu"))

print(student3.classs("Maks"))
print(student3.woot("Maks"))
print(student3.pain("Maks"))
