import os
import json

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/karvands.json"):
    data = {
        "bootcamp": "Karvand",
        "karvands": []
    }

    with open("data/karvands.json", "w") as file:
        json.dump(data, file, indent=4)

print("Project is ready.")