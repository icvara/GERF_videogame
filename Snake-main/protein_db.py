import json
import random

proteins = [
    {
        "name": "Hemoglobin",
        "description": "Carries oxygen in the blood.",
        "active_sites": [2, 4],
        "sequence": ["r", "r", "g", "b", "y"]
    },
    {
        "name": "Insulin",
        "description": "Regulates blood sugar levels.",
        "active_sites": [0],
        "sequence": ["g", "g", "y", "b"]
    },
    {
        "name": "Collagen",
        "description": "Structural protein in connective tissue.",
        "active_sites": [3],
        "sequence": ["b", "y", "r", "g"]
    }
]

with open("/Users/giorgiadelmissier/Desktop/GERF/GERF_videogame/Snake-main/proteins_db.json", "w") as f:
    json.dump(proteins, f, indent=4)
