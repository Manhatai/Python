serniczkowy_spam = {"pog@wp.pl":"Mateusz Pietkiewicz", "zjep@wp.pl": "Szymon Staś", "mati@wp.pl": "Andrzej Poniedzielski",}
print("Witaj w codziennych sernikach!")
y = input("Podaj imię i nazwisko: ")
x = input("Podaj swój e-mail: ")
serniczkowy_spam[x] = y

print("Oto dane wszystkich użytkowników:")
print(serniczkowy_spam)