# Wczytywanie pliku
with open('pantadeusz.txt', 'r', encoding='utf-8') as file:
    text = file.read()


print(text)

s = "   Tekst z białymi znakami na początku i na końcu   "
print(s.strip())

s = "To jest tekst podzielony na części"
print(s.split())
