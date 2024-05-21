import re
import sys

def usage():
    """Print the usage instructions for alfabet_items_check.py"""
    print("Usage: python alfabet_items_check.py <file_path_to_readme_file>")

def read_file(file_path):
    """Read the readme.md file contents"""
    return ''.join([line for line in open(file_path)])

def extract_items_from_code_block(file_content):
    """Extract key-value pairs from a code block."""
    pattern = r'```alfabet(.*?)```'
    match = re.search(pattern, file_content, re.DOTALL)
    items = {}
    if match:
        code_block_content = match.group(1)
        lines = code_block_content.split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                items[key] = value
    return items

def check_missing_items(items, required_items):
    """return the missing or empty items"""
    missing_items = []
    for required_item in required_items:
        if required_item not in items or items[required_item].strip() == '':
            missing_items.append(required_item)
    return missing_items

def print_missing_items(missing_items):
    """Print out the missing alfabet code or empty items"""
    if not missing_items:
        print("All items are filled out in the alfabet code block.")
    else:
        print("The following items are empty or missing in the alfabet code block:")
        print('\n'.join([f"- {missing_item}" for missing_item in missing_items]))
        sys.exit(1) # exit code to fail the azure pipeline execution

if __name__ == "__main__":
    if len(sys.argv) != 2: usage(), sys.exit(1)
    file_path = sys.argv[1]
    file_content = read_file(file_path)
    print(file_content)
    items = extract_items_from_code_block(file_content)
    required_items = ['Product', 'Owner', 'App-Id', 'Public exposure', 'Repo type', 'Status']
    missing_items = check_missing_items(items, required_items)
    print_missing_items(missing_items)