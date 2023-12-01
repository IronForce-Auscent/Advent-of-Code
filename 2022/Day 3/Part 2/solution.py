def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def split_string(string: str):
    return [string[:round(len(string)/2)], string[round(len(string)/2):]]

def get_common_items(group: list[str]):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item
    return "???"

def separate_groups(data: str):
    data = data.split()
    groups, group = [], []
    _count = 0
    while _count < len(data):
        group.append(data[_count])
        _count += 1
        if _count % 3 == 0 and _count > 0:
            groups.append(group)
            group = []
    return groups

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
    data = read_data()
    groups = separate_groups(data)
    print(groups)
    common_items = []
    for group in groups:
        common_items.append(get_common_items(group))
    priority_score = calculate_priority(common_items)
    print(common_items)
    print(priority_score)

if __name__ == "__main__":
    main()