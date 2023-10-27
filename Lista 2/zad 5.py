x = float(input("Podaj mg alkoholu w wydychanym powietrzu (w mg/l): "))

promile = x * 2.1

if promile <= 0.2:
    print("Możesz prowadzić samochód.")
elif promile > 0.2:
    print("Nie możesz prowadzić samochodu.")
