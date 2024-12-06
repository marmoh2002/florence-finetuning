import json
import re

def modify_descriptions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    for entry in data:
        if 'description' in entry:
            description = entry['description']['description']
            # Remove the "**Brief Description:**" section and everything up to "Detailed Description:"
            entry['description'] = re.sub(r"\*\*Brief Description:\*\*.*?Detailed Description:", "Detailed Description:", description, flags=re.DOTALL)
            # Remove all asterisks, newline characters, and hyphens
            entry['description'] = entry['description'].replace("*", "").replace("\n", " ").replace("-", "")
      
    with open("idk.json", 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
modify_descriptions('scene-0061.json')