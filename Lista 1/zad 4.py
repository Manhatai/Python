#zad 4

s = 1
min = 60 * s
g = 60 * min
d = 24 * g
m = 30 * d
r = 12 * m
dd = 5 * d ##dni dodatnie, tzn. 31,30,31,30 w dniach miesiaca, razem 7 dni - 2 dni lutego w roku nieprzestępnym
ddp = 6 * d ##dni dodatkowe w roku przestępnym

print("Liczba sekund w godzinach wynosi: ")
godzinyws = g * s
print(godzinyws)

print("Liczba sekund w dobie wynosi:")
sekundywd = d * s
print(sekundywd)

print("Liczba sekund w roku nieprzestępnym wynosi:")
sekundywrp = r * s + dd
print(sekundywrp)

print("Liczba sekund w roku przestępnym wynosi:")
sekundywrnp = r * s + ddp
print(sekundywrnp)

print("Liczba sekund w moim życiu wynosi około:") #od 18.06.2003 do 18.10.2022 minęły 232 miesiące
sekundywmż = (m * 232) * s
print(sekundywmż)
