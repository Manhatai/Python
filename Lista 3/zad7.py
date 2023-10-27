n = int(input("Wpisz liczbę kolejnych potęg liczby 2 którą chcesz zobaczyć: "))

print("Oto",n,"potęg liczby 2:")
for i in range(1, n + 1):
    print(2 ** i)
