#Postanowiłem wszystkie zadania z listy 9 upchnąć w jeden plik dla ułatwienia.
print("Zad1")
import random

pula = ["Manchester City", "Barcelona", "Liverpool", "Real Madryt", "PSG", "Atletico Madryt", "Chelsea",
        "Manchester United", "Atalanta", "Flamengo", "Palmeiras", "Bayern Monachium", "Benfica", "Inter Mediolan",
        "RB Lipsk", "Lech Poznań", "Śląsk Wrocław", "Raków Częstochowa", "Aston Villa", "Newcastle United"]

element = random.choices(pula, k=10)
element2 = random.choices(pula, k=10)
element3 = random.choices(pula, k=10)
element4 = random.choices(pula, k=10)
set1 = set()
set2 = set()
set3 = set()
set4 = set()


set1.update(element)
print(set1)
set2.update(element2)
print(set2)
set3.update(element3)
print(set3)
set4.update(element4)
print(set4)

print(".........................")
print("Zad2")
print(set1.difference(set2), set1.union(set2), set1.intersection(set2), set1.issuperset(set2), set1.issubset(set2))

print(".........................")
print("Zad3")
print("Długość zestawów to kolejno:", len(set1),len(set2),len(set3),len(set4))
set1.discard("PSG")
set2.discard("Atletico Madryt")
set3.discard("Liverpool")
set4.discard("Lech Poznań")

SubsetRes = set1 <= set2
SupersetRes = set3 >= set4

print(SubsetRes)
print(SupersetRes)

set1 = list(set1)
set2 = list(set2)
set3 = list(set3)
set4 = list(set4)

print(set1, set2, set3, set4) #Dzięki temu zyskujemy możliwość używania metod dostępnych tylko w listach, np. append lub randit z modułu random.
