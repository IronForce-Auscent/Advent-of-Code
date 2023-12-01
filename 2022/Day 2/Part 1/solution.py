def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def calculate_win(scenario: str):
    scenario = scenario.split()
    """
    Opponent
    A: Rock, B: Paper, C: Scissors

    You
    X: Rock, Y: Paper, Z: Scissors

    Possible lose conditions:
    A C
    B A
    C B

    Possible win conditions:
    A B
    B C
    C A
    """
    outcomes = {
        "A": {"X": 1+3, "Y": 2+6, "Z": 3+0},
        "B": {"X": 1+0, "Y": 2+3, "Z": 3+6}, 
        "C": {"X": 1+6, "Y": 2+0, "Z": 3+3}
    }
    return outcomes[scenario[0]][scenario[1]]

def main():
    data = read_data().split("\n")
    total_score = 0
    for scenario in data:
        total_score += calculate_win(scenario)
    print(total_score)

if __name__ == "__main__":
    main()