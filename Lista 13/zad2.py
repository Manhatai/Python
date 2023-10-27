ksiazki = []


class Library:
    def __init__(self, author, title, pages, cover, genre):
        self.author = author
        self.title = title
        self.pages = pages
        self.cover = cover
        self.genre = genre

    def read(self):
        return "Aktualnie czytana książka to {}.".format(self.title)

    def size(self):
        return "Książka {} ma {} stron.".format(self.title, self.pages)

    def author_(self):
        return "Książka {} została napisana przez {}".format(self.title, self.author)

    def coverngenre(self):
        return "Książka {} ma {} okładkę i jest gatunku {}".format(self.title, self.cover, self.genre)


book1 = Library("Jan Paradowski", "Mitologia Grecka", 320, "Twarda", "Historyczna")
book2 = Library("Sofokles", "Antygona", 100, "Miękka", "Dramat")
book3 = Library("Bolesław Prus", "Lalka", 550, "Twarda", "Filozoficzna")


def sortbysize():
    ksiazki.append(book1.pages)
    ksiazki.append(book2.pages)
    ksiazki.append(book3.pages)
    ksiazki.sort()


sortbysize()

print("Książka 1:")
print(book1.read())
print(book1.size())
print(book1.author_())
print(book1.coverngenre())
print()
print("Książka 2:")
print(book2.read())
print(book2.size())
print(book2.author_())
print(book2.coverngenre())
print()
print("Książka 3:")
print(book3.read())
print(book3.size())
print(book3.author_())
print(book3.coverngenre())
print()
print(ksiazki)
