import json
from pathlib import Path

def load_json(filepath):
    """Load JSON data from a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filepath):
    """Save data to a JSON file."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def extract_drugs(data):
    """Recursively extract drugs from the ATC hierarchy."""
    drugs = []
    if "children" in data:
        for child in data["children"]:
            if "drugbank_id" in child:  # It's a drug leaf node
                drugs.append({
                    "name": child["name"],
                    "atc_code": data["atc_code"],  # Parent's ATC is the drug's ATC
                    "drugbank_id": child["drugbank_id"]
                })
            else:
                drugs.extend(extract_drugs(child))
    return drugs

def main():
    # Paths (adjust as needed)
    input_path = Path('../processed/drugs_atc.json')
    output_path = Path('../processed/drugs_list.json')

    # Load, transform, and save
    atc_hierarchy = load_json(input_path)
    flattened_drugs = []
    for category in atc_hierarchy["classes"]:
        flattened_drugs.extend(extract_drugs(category))
    
    save_json(flattened_drugs, output_path)
    print(f"✅ Flattened {len(flattened_drugs)} drugs to {output_path}")

if __name__ == "__main__":
    main()