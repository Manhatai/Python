lista = []

x = int(input("Podaj liczbę: "))
lista.append(x)
print(lista)

while True:
 x = int(input("Podaj liczbę: "))
 if abs((lista[-1] - x)) < 5:
     print('ja nie moge')
     quit()
 else:
     lista.append(x)
     print(lista)
