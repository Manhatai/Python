meni = {"pizza_hawajska":19.99, "ziemniak":2, "spagetti z ziemniaka":5, "ziemniak_w_skórce":9.99, "ziemniak_z_masłem":10.99, "skórka_z_ziemniaka_z_masłem":7, "ziemniak_bez_skórki":10, "ziemniak_z_majonezem":12, 'ziemniak_z_ziemi':1, "pyry":50}

print("Obiady")
print(meni)
print("usuwamy hawajska jak cos")

print("Ceny")
for wartosc in meni.values():
    print(wartosc)

print("Obiady i ceny:")
for wartosc, klucz in meni.items():
    print(wartosc, klucz)
print("usuwamy hawajska jak cos")

del meni["pizza_hawajska"]
del meni["ziemniak_z_ziemi"]
x = input("Podaj nazwę nowego dania do menu: ")
y = int(input("Podaj cenę dania z menu: "))
meni[x]=y
print(meni)


