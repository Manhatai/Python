string = "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."
list1 = [" Zwinny", " lis", " przeskoczył", " nad", " leniwym", " psem", "."]
list2 = []
counter = 0
print(''.join(list1))
while True:
 for i in string:
    list2.append(i)
    counter = counter + 1
    if counter == 47:
     print(list2)
     quit()



#zad4
#Uważam że są to komendy użyteczne, szczególnie te które poprawiają wielkośc znaków, wykrywają dziwne znaki itd. Mogą być stosowane np przy podawaniu danych logowania.
