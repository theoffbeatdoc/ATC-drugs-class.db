# ATC Drugs Classification Database (a static JSON API)

A lightweight project that stores the Anatomical Therapeutic Chemical (ATC) drug classification data as JSON and provides easy access to the data, including mappings between Drug names, ATC codes, and DrugBank IDs, served via a CDN.

## Overview
This project offers:
- A comprehensive JSON dataset containing ATC drug classification information.
- Mappings between Drug names, ATC codes, and DrugBank IDs for cross-referencing drug information.
- A public CDN endpoint to fetch the JSON data for integration into applications, research, or educational tools.
- Easy-to-use format suitable for web and backend applications.


## ATC Drug Classification
- (refer to [Anatomical Therapeutic Chemical (ATC) Classification](https://www.who.int/tools/atc-ddd-toolkit/atc-classification) for more details.)
- In the Anatomical Therapeutic Chemical (ATC) classification system, the active substances are divided into different groups according to the organ or system on which they act and their therapeutic, pharmacological and chemical properties. Drugs are classified in groups at five different levels.
- **ATC 1st level**
	- The system has fourteen main anatomical or pharmacological groups (1st level). The ATC 1st levels are shown in the figure.
- **ATC 2nd level**
	- Pharmacological or Therapeutic subgroup
- **ATC 3rd& 4th levels**
	- Chemical, Pharmacological or Therapeutic subgroup
- **ATC 5th level**
	- Chemical substance

![atcclassification](https://www.who.int/images/default-source/departments/essential-medicines/atcclassification.tmb-768v.jpg?Culture=en&sfvrsn=1c90541b_2 "atcclassification")

The 2nd, 3rd and 4th levels are often used to identify pharmacological subgroups when that is considered more appropriate than therapeutic or chemical subgroups.

The complete classification of metformin illustrates the structure of the code:
![metformin-structure](https://www.who.int/images/default-source/departments/essential-medicines/table1.jpg?sfvrsn=4e770104_0)


## Why This Project?
The ATC classification system is widely used in pharmacology and drug research to classify drugs into different groups according to the organ or system they act on and their therapeutic, pharmacological, and chemical properties.

This project makes it simple to:
- Access and integrate ATC classification data programmatically.
- Link ATC codes with DrugBank IDs for enriched drug data.
- Use a reliable CDN for fast and scalable access to data.

## Data Files, Structure & CDN links
- The `db` folder contains the structured polished json databases.
### 1. ATC Classes (Hierarchical)
- Broad ATC classes with nested subgroups down to drugs.
- Useful for exploring the full classification tree.

```CDN
https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/drugs_atc.json
```

```json
{
  "classes": [
    {
      "name": "Alimentary tract and metabolism (A)",
      "atc_code": "A",
      "children": [
        {
          "name": "Other alimentary tract and metabolism products (A16)",
          "atc_code": "A16",
          "children": [
            {
              "name": "Various alimentary tract and metabolism products (A16AX)",
              "atc_code": "A16AX",
              "children": [
                {
                  "name": "Nedosiran (A16AX25)",
                  "atc_code": "A16AX25",
                  "children": [
                    {
                      "name": "Nedosiran",
                      "drugbank_id": "DB17635"
                    }
                    ...
                    ...
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### 2. ATC Subgroups (Hierarchical)
- Separate JSON for subgroup hierarchies with detailed nesting.
- Contains groups, subgroups, and drug entries with DrugBank IDs.

```CDN
https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/classes/<ATC Class level 1 or level 2>.json

https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/classes/A.json
https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/classes/A01.json
```


```json
[
  {
    "name": "Stomatological preparations (A01)",
    "atc_code": "A01",
    "children": [ ... ]
  }
]
```


### 3. Flattened Drug List (Array)
- A flat list of drugs, each with its name, ATC code, and DrugBank ID.
- Useful for quick lookups, searches, and alphabetical listings.

```
https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/drugs_list.json
```


```json
[
  {
    "name": "Nedosiran",
    "atc_code": "A16AX25",
    "drugbank_id": "DB17635"
  },
  {
    "name": "Gavorestat",
    "atc_code": "A16AX24",
    "drugbank_id": "DB16707"
  }
  ...
  ...
]

```

### 4. Alphabetical Lists
- Drugs sorted alphabetically by name (provided as a separate JSON file).
- Enables easy navigation and search by drug name.

```CDN
https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db//lists/drugs-letter-<LETTER>.json

https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db//lists/drugs-letter-A.json
```

## Usage Examples

### Fetching data from the CDN

```js
// Fetch hierarchical classes JSON
fetch("https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/drugs_atc.json")
  .then(res => res.json())
  .then(data => console.log(data.classes));

// Fetch subgroups JSON
fetch("https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/classes/A01.json")
  .then(res => res.json())
  .then(data => console.log(data));

// Fetch flattened drug list
fetch("https://cdn.jsdelivr.net/gh/theoffbeatdoc/ATC-drugs-class.db@main/db/drugs_list.json")
  .then(res => res.json())
  .then(drugs => {
    // Find drug by name
    const nedosiran = drugs.find(d => d.name === "Nedosiran");
    console.log(nedosiran);
  });

```

---
### Offline integration
Download any of the JSON files and import into your project or database for offline queries.

---

## Why Use This Data?
- **Multi-format JSON** enables flexibility for different use cases:
    - Hierarchical structures for classification trees.
    - Flattened lists for fast lookup and alphabetical browsing.
- **ATC to DrugBank ID mapping** enriches the drug information.
- Data accessible via CDN for reliable, scalable usage.
- Ideal for healthcare applications, research, and educational tools.

---

## Contribution
Improvements, bug fixes, new mappings, or updates are very welcome. Please fork the repo and submit pull requests or open issues.

---
## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format.
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

See the [LICENSE](LICENSE) file for full details.

---
## Contact

Questions? Suggestions? Open an issue or contact [drkoustavsinharay@gmail.com].

---

_Providing accessible, structured drug classification data for developers and researchers._