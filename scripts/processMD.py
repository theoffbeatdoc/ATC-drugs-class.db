import re
import json
from pathlib import Path

def parse_markdown_to_json(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        lines = [line.expandtabs(4).rstrip() for line in f if line.strip()]

    root = {'classes': []}
    stack = []
    drugbank_id_pattern = re.compile(r'drugs/(DB\d+)')

    for line in lines:
        # Normalize indentation
        indent = len(line) - len(line.lstrip(' '))
        level = indent // 4  # treat every 4 spaces as one level

        # Parse markdown link
        match = re.match(r'^\s*-\s+\[([^\]]+)\]\(([^)]+)\)', line.strip())
        if not match:
            continue

        raw_name, url = match.groups()
        clean_name = raw_name.strip('*')
        node = {'name': clean_name}

        # Extract ATC code if present
        atc_match = re.search(r'\(([A-Z]\d{2}[A-Z]{0,2}\d{0,2})\)$', clean_name)
        if atc_match:
            node['atc_code'] = atc_match.group(1)

        # Extract DrugBank ID if present
        if 'drugbank.com/drugs/' in url:
            drugbank_match = drugbank_id_pattern.search(url)
            if drugbank_match:
                node['drugbank_id'] = drugbank_match.group(1)

        # Adjust stack based on current level
        while len(stack) > level:
            stack.pop()

        if stack:
            parent = stack[-1]
            parent.setdefault('children', []).append(node)
        else:
            root['classes'].append(node)

        # Only push to stack if this node can have children
        if 'drugbank_id' not in node:
            stack.append(node)

    # Clean empty children arrays
    def clean(node):
        if 'children' in node:
            node['children'] = [clean(child) for child in node['children']]
            if not node['children']:
                del node['children']
        return node

    root['classes'] = [clean(cls) for cls in root['classes']]
    return root

def save_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    input_path = Path('../raw/ATCdrugsWithDrugBankLinks.md')
    output_path = Path('../processed/drugs_atc.json')
    
    output_path.parent.mkdir(exist_ok=True)
    
    data = parse_markdown_to_json(input_path)
    save_json(data, output_path)
    print(f"Successfully converted markdown to JSON at {output_path}")

if __name__ == '__main__':
    main()
