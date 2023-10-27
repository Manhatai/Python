def read_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
    except FileNotFoundError as e:
        print(e)
        return None

    max_lines = max(len(lines1), len(lines2))
    result = []

    for i in range(max_lines):
        if i < len(lines1):
            result.append(lines1[i].strip())
        if i < len(lines2):
            result.append(lines2[i].strip())

    return result


def write_to_file(filename, lines):
    try:
        with open(filename, 'w') as f:
            for line in lines:
                f.write(line + '\n')
    except Exception as e:
        print(f"Problem z zapisem do pliku: {e}")


def main():
    file1 = input("Podaj nazwę pierwszego pliku: ")
    file2 = input("Podaj nazwę drugiego pliku: ")

    lines = read_files(file1, file2)
    if lines is not None:
        write_to_file('wynik.txt', lines)


if __name__ == "__main__":
    main()
