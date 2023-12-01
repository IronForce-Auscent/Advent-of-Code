def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def calculate_win(scenario: str):
    scenario = scenario.split()
    score_values = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
    score = 0
    if scenario[1] == "X":
        score += score_values[scenario[1]]
        if scenario[0] == "A":
            score += score_values["C"]
        elif scenario[0] == "B":
            score += score_values["A"]
        else:
            score += score_values["B"]
    elif scenario[1] == "Y":
        score += score_values[scenario[0]]
        score += score_values[scenario[1]]
    elif scenario[1] == "Z":
        score += score_values[scenario[1]]
        if scenario[0] == "A":
            score += score_values["B"]
        elif scenario[0] == "B":
            score += score_values["C"]
        else:
            score += score_values["A"]
    else:
        print("WTF?")
        return False
    return score
    
def main():
    data = read_data().split("\n")
    total_score = 0
    for scenario in data:
        total_score += calculate_win(scenario)
    print(total_score)

if __name__ == "__main__":
    main()