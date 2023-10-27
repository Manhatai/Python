import numpy as np

lista = []

while True:
    x = int(input("Podaj początek zakresu liczb: "))
    y = int(input("Podaj koniec zakresu liczb: "))
    if y < 6:
        print("Nie możesz wpisać zakresu mniejszego niż 6 liczb")
        continue
    for i in range(x, y+1):
        lista.append(i)
    print('Oto pierwsze 6 liczb z wpisanego zakresu:')
    print(lista[:6])
    break


print("Oto minimum tych liczb:")
print(min(lista[:6]))
print("Oto maksimum tych liczb:")
print(max(lista[:6]))
print("Oto mediana tych liczb:")
print(np.median(lista[:6]))
print("Oto średnia tych liczb:")
print(np.mean(lista[:6]))
quit()
