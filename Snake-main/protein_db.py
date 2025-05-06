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
        "active_sites": [0, 3],
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
        "active_sites": [],
        "sequence": ["b", "y", "r", "g"]
    }
]

with open(f"{current_dir}/proteins_db.json", "w") as f:
    json.dump(proteins, f, indent=4)
