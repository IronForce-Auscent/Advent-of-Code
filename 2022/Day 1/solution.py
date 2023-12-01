def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def calculate_calories(data):
    calorie_list = []
    for entry in data:
        snacks = entry.split("\n")
        calorie_sum = 0
        for snack in snacks:
            calorie_sum += int(snack)
        calorie_list.append(calorie_sum)
    return calorie_list

def main():
    document = read_data().split("\n\n")
    calorie_list = calculate_calories(document)
    calorie_list.sort(reverse=True)
    print(calorie_list[0] + calorie_list[1] + calorie_list[2])

if __name__ == "__main__":
    main()