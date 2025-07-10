import json
import os

# Path to the main input JSON file
input_file_path = '../processed/drugs_atc.json'

# Output directory to save the separate JSON files
output_dir = '../db/classes'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def save_json(data, filename):
    """Helper function to save data to a JSON file."""
    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Saved: {filename}")

def process_classes(classes):
    """Process the main classes and second-level classes."""
    # Dictionary to store top-level and second-level atc_codes
    top_level_classes = {}
    second_level_classes = {}

    for main_class in classes:
        # Top-level atc_code (e.g., A, B, etc.)
        top_code = main_class['atc_code']
        top_level_classes[top_code] = main_class
        
        # Now process second-level classes (e.g., A16, A17, etc.)
        if 'children' in main_class:
            for second_class in main_class['children']:
                second_code = second_class['atc_code']
                second_level_classes[second_code] = second_class
    
    # Save top-level and second-level classes as separate JSON files
    for code, class_data in top_level_classes.items():
        save_json([class_data], f"{code}.json")
    
    for code, class_data in second_level_classes.items():
        save_json([class_data], f"{code}.json")

def main():
    # Load the main JSON file
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Extract the 'classes' list
    classes = data.get('classes', [])
    
    if not classes:
        print("No 'classes' found in the JSON file!")
        return
    
    # Process the classes and save them
    process_classes(classes)
    print("Processing completed.")

# Run the main function
if __name__ == '__main__':
    main()
