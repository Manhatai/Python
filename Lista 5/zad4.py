x = int(input("Podaj ilość liczb którą zamierzasz wpisać: "))
licznik = 0

while True:
 y = int(input("Podaj liczbę: "))
 licznik = licznik + 1
 if -6 < y < 6:   #Zakładam że chodzi o przedział <-6,6>, a nie (-6,6)
     print("Liczba znajduje się w przedziale <-6,6>")
 else:
     print("Liczba nie znajduje się w przedziale <-6,6>")
 if licznik == x:
     print("Wpisałeś max. ilość liczb.")
     break
