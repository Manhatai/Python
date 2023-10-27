def przelicznik():
    x = float(input("Podaj ilość stup uwu: "))
    cm = x * 30.48
    mm = x * 304.8
    km = x / 3280.8398950131
    print("Jest to:")
    print(cm, "centymetrów")
    print(mm, "milimetrów")
    print(km, "kilometrów")

przelicznik()