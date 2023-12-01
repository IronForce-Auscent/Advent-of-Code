def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def split_into_pairs(data: str):
    return data.split("\n")

def calculate_overlap(pair_input: str):
    new_pair = pair_input.split(",")
    pair = []
    for entry in new_pair:
        pair.append(entry.split("-"))
    pair = [[int(val) for val in sublist] for sublist in pair] # Thank you ChatGPT, forgot to convert string to integer
    pair_ranges = [[x for x in range(pair[0][0], pair[0][1] + 1)], [y for y in range(pair[1][0], pair[1][1] + 1)]]
    for value in pair_ranges[0]:
        if value in pair_ranges[1]:
            return True
        else:
            pass
    return False

def main():
    data = read_data()
    pairs = split_into_pairs(data)
    overlaps = 0
    for pair in pairs:
        overlap = calculate_overlap(pair)
        print(overlap)
        if overlap:
            overlaps += 1
    print(overlaps)

if __name__ == "__main__":
    #print(calculate_overlap([]))
    main()