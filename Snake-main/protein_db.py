import json
import random
from pathlib import Path

# Path to the current file
current_file = Path(__file__)

# Directory containing the file
current_dir = current_file.parent

proteins = [
    {
        "name": "Hemoglobin",
        "description": "Carries oxygen in the blood.",
        "sequence": ["r", "r", "g", "b", "y"]
    },
    {
        "name": "Insulin",
        "description": "Regulates blood sugar levels.",
        "sequence": ["g", "g", "y", "b"]
    },
    {
        "name": "Collagen",
        "description": "Structural protein in connective tissue.",
        "sequence": ["b", "y", "r", "g"]
    }
]

# Automatically assign 1–2 active site positions at random
for protein in proteins:
    length = len(protein["sequence"])
    num_active = min(2, length)
    protein["active_sites"] = random.sample(range(length), num_active)

with open(f"{current_dir}/proteins_db.json", "w") as f:
    json.dump(proteins, f, indent=4)
