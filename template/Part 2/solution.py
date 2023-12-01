def read_data():
    with open("testcases.txt", "r") as f:
        document = f.read()
    return document

def main():
    data = read_data()

if __name__ == "__main__":
    main()