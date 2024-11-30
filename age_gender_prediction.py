import os

import requests

OS = os.name

command_prefix = 'cls'

if OS == "posix":
    command_prefix = 'clear'

MENU = ("-------------------------\n"
        "Age and gender prediction\n"
        "-------------------------\n"
        "1) Predict Gender\n"
        "2) Predict Age\n"
        ".\n"
        "9) Quit\n")

choice = 0

while choice != 9:
    print(MENU)
    choice = int(input("Choice: "))
    os.system(command_prefix)

    while choice not in [1, 2, 9]:
        print("Choose between 1, 2 or 9 !")
        ok = input("Continue [ENTER]")

        os.system(command_prefix)

        pass

        print('pas pass')

        print(MENU)
        choice = int(input("Choice: "))

        os.system(command_prefix)

    if choice == 1:
        name = input("Predict the gender of a name: ")

        os.system(command_prefix)

        request_gender = f"https://api.genderize.io?name={name}"

        r = requests.get(request_gender)
        gender_data = r.json()

        print(
            f"{gender_data['name'].upper()} is {gender_data['gender'].upper()} "
            f"with {int(gender_data['probability'] * 100)}% certainty.\n")

    elif choice == 2:
        name = input("\nPredict the age of a name: ")

        os.system(command_prefix)

        request_age = f"https://api.agify.io?name={name}"

        r = requests.get(request_age)
        age_data = r.json()

        print(f"{age_data['name'].upper()} is {age_data['age']} years old.\n")

    quit_menu = input("Continue? [y/n]: ")

    if quit_menu.lower() == 'n':
        choice = 9
    else:
        os.system(command_prefix)
