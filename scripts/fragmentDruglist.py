import json
from pathlib import Path
from collections import defaultdict

def load_json(filepath):
    """Load JSON data from a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filepath):
    """Save data to a JSON file."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def fragment_drugs_by_letter(drugs_list):
    """Group drugs by the first letter of their name."""
    letter_groups = defaultdict(list)
    for drug in drugs_list:
        first_letter = drug["name"][0].upper()  # Ensure uppercase (e.g., 'A' for 'aspirin')
        letter_groups[first_letter].append(drug)
    return letter_groups

def main():
    # Paths
    input_path = Path('../processed/drugs_list.json')
    output_dir = Path('../db/lists/')

    # Load data
    drugs_list = load_json(input_path)

    # Group by first letter
    letter_groups = fragment_drugs_by_letter(drugs_list)

    # Save each group
    for letter, drugs in letter_groups.items():
        output_path = output_dir / f'drugs-letter-{letter}.json'
        save_json(drugs, output_path)
        print(f"✅ Saved {len(drugs)} drugs to {output_path}")

if __name__ == "__main__":
    main()