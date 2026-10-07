import os
import json


DATA_DIR = "data"
FILE = os.path.join(DATA_DIR, "karvands.json")


def create_initial_file():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(FILE):
        data = {
            "karvands": []
        }

        with open(FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def load_data():
    create_initial_file()

    try:
        with open(FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict) or "karvands" not in data:
            raise ValueError

        if not isinstance(data["karvands"], list):
            raise ValueError

        return data

    except (json.JSONDecodeError, ValueError):
        print("JSON file is broken. Initial structure created.")

        data = {
            "karvands": []
        }

        save_data(data)

        return data


def save_data(data):
    create_initial_file()

    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_next_id(karvands):
    if not karvands:
        return 1

    max_id = max(karvand["id"] for karvand in karvands)
    return max_id + 1


def get_skill_score():
    while True:
        try:
            score = int(input("Skill score (0 to 100): "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")


def add_karvand():
    data = load_data()

    name = input("Full name: ")
    email = input("Email: ")
    city = input("City: ")
    degree = input("Degree: ")
    field = input("Field of study: ")
    skill_name = input("Skill name: ")
    skill_level = input("Skill level: ")
    score = get_skill_score()

    new_id = get_next_id(data["karvands"])

    karvand = {
        "id": new_id,
        "name": name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "field": field
        },
        "skills": [
            {
                "name": skill_name,
                "level": skill_level,
                "score": score
            }
        ]
    }

    data["karvands"].append(karvand)
    save_data(data)

    print("Karvand added successfully.")
    print("Karvand ID:", new_id)


def show_karvands():
    data = load_data()

    if not data["karvands"]:
        print("No karvands registered.")
        return

    for karvand in data["karvands"]:
        print("-" * 40)
        print("ID:", karvand["id"])
        print("Name:", karvand["name"])
        print("Email:", karvand["email"])
        print("City:", karvand["city"])

        print("Degree:", karvand["education"]["degree"])
        print("Field of study:", karvand["education"]["field"])

        print("Skills:")

        for skill in karvand["skills"]:
            print("  Name:", skill["name"])
            print("  Level:", skill["level"])
            print("  Score:", skill["score"])

    print("-" * 40)


def main():
    load_data()

    while True:
        print("\n1. Add karvand")
        print("2. Show karvands")
        print("8. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_karvand()

        elif choice == "2":
            show_karvands()

        elif choice == "8":
            print("Exit")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()