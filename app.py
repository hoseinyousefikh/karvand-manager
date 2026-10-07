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


def find_karvand_by_id():
    data = load_data()
    while True:
        try:
            karvand_id = int(input("Karvand ID: "))
            break
        except ValueError:
            print("Please enter a number.")

    for karvand in data["karvands"]:
        if karvand["id"] == karvand_id:
            print("-" * 40)
            print("ID:", karvand["id"])
            print("Name:", karvand["name"])
            print("Email:", karvand["email"])
            print("City:", karvand["city"])
            print("Education:", karvand["education"])
            print("Skills:", karvand["skills"])
            print("-" * 40)
            return
    print("No karvand found with this ID.")

def find_karvands_by_skill():
    data = load_data()
    skill_name = input("Skill name: ").strip()
    found = False
    for karvand in data["karvands"]:
        for skill in karvand["skills"]:
            if skill["name"].lower() == skill_name.lower():
                print("-" * 40)
                print("ID:", karvand["id"])
                print("Name:", karvand["name"])
                print("Email:", karvand["email"])
                print("City:", karvand["city"])
                print("Education:", karvand["education"])
                print("Skills:", karvand["skills"])
                found = True
                break

    if not found:
        print("No karvand found with this skill.")


def edit_karvand():
    data = load_data()
    while True:
        try:
            karvand_id = int(input("Karvand ID: "))
            break
        except ValueError:
            print("Please enter a number.")

    karvand = None
    for item in data["karvands"]:
        if item["id"] == karvand_id:
            karvand = item
            break
    if karvand is None:
        print("No karvand found with this ID.")
        return

    print("\nWhat do you want to edit?")
    print("1. Email")
    print("2. City")
    print("3. Degree")
    print("4. Field of study")
    print("5. Edit multiple fields")
    choice = input("Choice: ")

    if choice == "1":
        karvand["email"] = input("New email: ")

    elif choice == "2":
        karvand["city"] = input("New city: ")

    elif choice == "3":
        karvand["education"]["degree"] = input("New degree: ")

    elif choice == "4":
        karvand["education"]["field"] = input("New field of study: ")

    elif choice == "5":
        email = input("New email: ")
        city = input("New city: ")
        degree = input("New degree: ")
        field = input("New field of study: ")
        karvand["email"] = email
        karvand["city"] = city
        karvand["education"]["degree"] = degree
        karvand["education"]["field"] = field

    else:
        print("Invalid option.")
        return
    save_data(data)
    print("Karvand information edited successfully.")


def delete_karvand():
    data = load_data()
    while True:
        try:
            karvand_id = int(input("Karvand ID: "))
            break
        except ValueError:
            print("Please enter a number.")

    for index, karvand in enumerate(data["karvands"]):
        if karvand["id"] == karvand_id:
            data["karvands"].pop(index)
            save_data(data)
            print("Karvand deleted successfully.")
            return

    print("No karvand found with this ID.")


def generate_report():
    data = load_data()
    karvands = data["karvands"]
    total_karvands = len(karvands)
    total_skills = 0
    scores = []
    cities = []
    unique_skills = []

    for karvand in karvands:
        cities.append(karvand["city"])
        for skill in karvand["skills"]:
            total_skills += 1
            scores.append(skill["score"])

            if skill["name"] not in unique_skills:
                unique_skills.append(skill["name"])

    unique_cities = []

    for city in cities:
        if city not in unique_cities:
            unique_cities.append(city)
    if scores:
        average_skill_score = sum(scores) / len(scores)
    else:
        average_skill_score = 0
    report = {
        "total_karvands": total_karvands,
        "total_skills": total_skills,
        "average_skill_score": average_skill_score,
        "cities": unique_cities,
        "unique_skills": unique_skills
    }

    report_file = os.path.join(DATA_DIR, "report.json")
    with open(report_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("\nGeneral report")
    print("-" * 40)
    print("Total karvands:", total_karvands)
    print("Total skills:", total_skills)
    print("Average skill score:", average_skill_score)
    print("Cities:", unique_cities)
    print("Unique skills:", unique_skills)
    print("-" * 40)
    print("Report saved in data/report.json.")


def main():
    load_data()

    while True:
        print("\n1. Add karvand")
        print("2. Show karvands")
        print("3. Find karvand by ID")
        print("4. Find karvands by skill")
        print("5. Edit karvand")
        print("6. Delete karvand")
        print("7. General report")
        print("8. Exit")
        choice = input("Choice: ")

        if choice == "1":
            add_karvand()

        elif choice == "2":
            show_karvands()

        elif choice == "3":
            find_karvand_by_id()

        elif choice == "4":
            find_karvands_by_skill()

        elif choice == "5":
            edit_karvand()

        elif choice == "6":
            delete_karvand()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            print("Exit")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()