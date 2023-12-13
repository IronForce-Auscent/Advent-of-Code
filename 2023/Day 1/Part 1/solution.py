def read_data():
    with open("sample.txt", "r") as f:
        data = f.read()
    return data

def get_first_and_last_numbers(string: str):
    valid_ints = []
    for char in string:
        if char.isnumeric():
            valid_ints.append(char)
    res = str(valid_ints[0]) + str(valid_ints[-1])
    return int(res)

def main(data):
    calibration_values = []
    for string in data.split():
        calibration_values.append(get_first_and_last_numbers(string))
    final_value = 0
    for value in calibration_values:
        final_value += value
    print(final_value)
