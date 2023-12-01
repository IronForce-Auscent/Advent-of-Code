valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def read_document():
    with open("sample.txt", "r") as f:
        document = f.read()
    return document

def get_first_and_last_numbers(string: str):
    valid_ints = []
    for char in string:
        if char.isnumeric():
            valid_ints.append(char)
    res = str(valid_ints[0]) + str(valid_ints[-1])
    return int(res)

def get_valid_integers_in_string(string: str):
    valid_ints = []
    for pos in range(len(string)):     
        if string[pos].isnumeric():
            valid_ints.append(string[pos])

        for i, word in enumerate(valid_digits):
            if string[pos:pos + len(word)] == word:
                valid_ints.append(int(i + 1))
    return valid_ints

def part2():
    document = read_document().split()
    final_value = 0
    for string in document:
        valid_integers = get_valid_integers_in_string(string)
        final_value += int(str(valid_integers[0]) + str(valid_integers[-1]))
    print(final_value)

if __name__ == "__main__":
    part2()