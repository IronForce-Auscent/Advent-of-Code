class Sample():
    cargo_ship = [
    # Represented from bottom to top
        [], # Empty list, reduces workload when doing calculations for moving crates
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]
    instructions = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2  
"""