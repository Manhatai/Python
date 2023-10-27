def BMI():
    x = float(input("Podaj swoją masę w kg: "))
    y = float(input("Podaj swój wzorst w metrach: "))
    BMI = x / (y**2)
    if BMI < 18.5:
        print("Masz niedowagę!")
    elif 18.5 < BMI < 24.99:
        print("Twoja waga jest prawidłowa!")
    elif BMI > 25:
        print("Masz nadwagę!")
    print(BMI)
BMI()
