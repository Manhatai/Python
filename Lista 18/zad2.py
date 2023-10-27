with open('pantadeusz.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines = text.splitlines()

selected_lines = [7, 11, 59, 97, 103]
for i in selected_lines:
    if i < len(lines):
        print(lines[i])
    else:
        print(f"Indeks {i} przekracza zakres listy.")


print(f"Liczba wierszy: {len(lines)}")

for i, line in enumerate(lines, start=1):
    print(f"{i}: {line}")
