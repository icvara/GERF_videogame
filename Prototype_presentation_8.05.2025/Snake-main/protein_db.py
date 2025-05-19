import json
import random
from pathlib import Path

# Path to the current file
current_file = Path(__file__)

# Directory containing the file
current_dir = current_file.parent

proteins = [
    {
        "name": "Casein",
        "description": "Main protein in milk — gives cheese its texture!",
        "active_sites": [0],
        "sequence": ["c", "s", "q", "d", "f", "x"]
    },
    {
        "name": "Leghemoglobin",
        "description": "Makes plant-based burgers look and taste like meat!",
        "active_sites": [1, 4],
        "sequence": ["c", "d", "d", "s", "f"]
    },
    {
        "name": "Mycoprotein",
        "description": "Fungi-based protein used in meat alternatives like burgers and nuggets.",
        "active_sites": [4],
        "sequence": ["c", "q", "d", "x"]
    }
]

with open(f"{current_dir}/proteins_db.json", "w") as f:
    json.dump(proteins, f, indent=4)
