def check_user(username):
    "Ellenőrzi, hogy létezik-e a felhasználó."
    with open("users.csv", "r", encoding="utf-8") as file:
        for line in file:
            user = line.strip().split(";")
            if user[0] == username:
                return user[1]
    return ""

def check_password(password, max_proba, prompt):
    "Ellenőrzi a jelszót és visszatér a belépés sikerességével."
    proba = 0
    while proba < max_proba:
        bevitel = input(prompt)
        if bevitel == password:
            return True
        else:
            print("Hibás jelszó, próbálja újra.")
            proba += 1
    return False

def login():
    "A belépési folyamat vezérlése."
    login_success = True
    password = check_user(input("Kérem a felhasználónevet: "))

    if password == "":
        print("Nincs ilyen felhasználó, regisztrálj!")
        login_success = False
    else:
        if not check_password(password, 3, "Kérem a jelszót: "):
            print("Nem megfelelő a jelszó!")
            login_success = False

    return login_success