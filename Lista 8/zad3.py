loginy_hasla = {"Maciej": "klocek321", "Marcel": "qwerty", "Marcelina": "jd69", "Magdalena": "2137prayge", "Mirosław": "jebacmatmeelo", "admin": "admin",}
while True:
 x = input("Podaj login: ")
 y = input("Podaj haslo: ")
 strona = "www.twojanajgorszapraca.pl"
 panel_admina = "www.CENZURA.pl"
 for login, haslo in loginy_hasla.items():
    if x == login:
        print("Login jest prawidłowy.")
    else:
        continue
    if y == haslo:
        print("Haslo jest prawidłowe.")
    else:
        continue
    if x == "admin" and y == "admin":
        print("Witaj, za chwilę zostaniesz przekierowany na",panel_admina,)
        quit()
    if x == login and y == haslo:
        print("Witaj w robocie! Zostaniesz za chwilę przekierowany na stronę",strona,)
        quit()
