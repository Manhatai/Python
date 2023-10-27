# Napisz program przy użyciu pętli while wyświetlający na ekranie liczby od 254 do 320, ale niepodzielne przez 2 ale podzielne przez 5.
x = 254
while x <= 320:
    if x % 2 != 0:
        if x % 5 == 0:
          print(x)
    x+=1

y=-320
while y <= -254:
    if y % 2 != 0:
        if y % 5 == 0:
            print(y)
    y+=1
