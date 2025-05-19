import json
import random
from pathlib import Path

random.seed(1234)

# Path to the current file
current_file = Path(__file__)

# Directory containing the file
current_dir = current_file.parent

letters = ["c", "s", "q", "x", "f", "d"]
length = random.randint(15, 30)

proteins = [
  {
    "name": "Casein",
    "description": "Casein is the main protein in milk, which gives cheese its stretchy texture!",
    "sequence": random.choices(letters, k=length),
    "active_sites": [5,6,7]
  },
  {
    "name": "Leghemoglobin",
    "description": "Leghemoglobin comes from soybean roots but it can make plant burgers “bleed” like real meat!",
    "sequence": random.choices(letters, k=length),
    "active_sites": [1,2,3]
  },
  {
    "name": "Mycoprotein",
    "description": "Mycoproteins are found in fungi but are used in meat alternatives like Quorn to give it a naturally meaty texture!",
    "sequence": random.choices(letters, k=length),
    "active_sites": []
  },
  {
    "name": "Soy glycinin",
    "description": "Glycinin is one of soy’s main proteins and helps tofu hold its shape!",
    "sequence": random.choices(letters, k=length),
    "active_sites": []
  },
  {
    "name": "Wheat gluten",
    "description": "Gluten is an elastic protein found in wheat - it makes seitan chewy and bread dough stretchy!",
    "sequence": random.choices(letters, k=length),
    "active_sites": [8,9,10,13,14]
  },
  {
    "name": "Miraculin",
    "description": "Miraculin is a protein from the miracle fruit that makes sour foods taste sweet!",
    "sequence": random.choices(letters, k=length),
    "active_sites": [8,9]
  },
  {
    "name": "Monellin",
    "description": "Monellin is a sweet protein from the serendipity berry that is about 3000 times sweeter than sugar!",
    "sequence": random.choices(letters, k=length),
    "active_sites": [-4,-5,-6]
  },
  {
    "name": "Phycocyanin",
    "description": "Phycocyanin is a protein found in spirulina, which can make smoothies and snacks bright blue-green all by itself—no artificial dye needed!!",
    "sequence": random.choices(letters, k=length),
    "active_sites": [-8, -9]
  },
  {
    "name": "Pea globulin",
    "description": "Pea globulin can act like egg whites in baking, helping make vegan meringues and fluffy cakes without any eggs!",
    "sequence": random.choices(letters, k=length),
    "active_sites": []
  },
  {
    "name": "Hemp protein",
    "description": "This protein is made from hemp seeds and contains all nine essential amino acids to help muscles repair and grow after exercise!",
    "sequence": random.choices(letters, k=length),
    "active_sites": []
  }
]

with open(f"{current_dir}/proteins_db.json", "w") as f:
    json.dump(proteins, f, indent=4)
