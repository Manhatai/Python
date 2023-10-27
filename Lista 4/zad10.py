lista = []

x = int(input("Podaj liczbę: "))
lista.append(x)
print('Suma liczb:')
print(lista[-1])

while True:
 x = int(input("Podaj liczbę: "))
 if lista[-1] == x:
     print('ja nie moge')
     quit()
 else:
     for i in lista:
         i = i + x
     lista.append(i)
     print('Suma liczb:')
     print(lista[-1])