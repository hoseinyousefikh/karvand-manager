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

        with open(FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return data


def save_data(data):
    create_initial_file()

    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    data = load_data()

    print("Karvand management program")
    print("Number of registered Karvands:", len(data["karvands"]))


if __name__ == "__main__":
    main()