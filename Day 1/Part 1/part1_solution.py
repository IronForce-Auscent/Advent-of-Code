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

def main():
    document = read_document().split()
    calibration_values = []
    for string in document:
        calibration_values.append(get_first_and_last_numbers(string))
    final_value = 0
    for value in calibration_values:
        final_value += value
    print(final_value)

if __name__ == "__main__":
    main()