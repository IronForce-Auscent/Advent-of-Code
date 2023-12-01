def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def split_string(string: str):
    return [string[:round(len(string)/2)], string[round(len(string)/2):]]

def get_common_items(entry_1: str, entry_2: str):
    for item_1 in entry_1:
        for item_2 in entry_2:
            if item_1 == item_2:
                return item_1
            else:
                pass
    return "???"

def calculate_priority(common_items: list[str]):
    priority_score = 0
    for item in common_items:
        if item.islower():
            priority_score += ord(item) - 96
        elif item.isupper():
            priority_score += ord(item) - 38
        else:
            return "HUH???"
    return priority_score

def main():
    data = read_data().split()
    common_items = []
    for entry in data:
        split_entry = split_string(entry)
        common_items.append(get_common_items(split_entry[0], split_entry[1]))
    priority_score = calculate_priority(common_items)
    print(priority_score)

if __name__ == "__main__":
    main()