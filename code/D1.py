def find_floor(instructions: str) -> int:
    floor = 0
    for char in instructions:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor


def find_basement_entry(instructions: str) -> int:
    floor = 0
    for position, char in enumerate(instructions, 1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return position
    return None  # Santa never enters the basement with the given instructions


if __name__ == "__main__":
    # First part
    with open("./input/D1.txt", "r") as file:
        instructions = file.readline().strip()

    floor = find_floor(instructions)
    print(f"Santa is going to floor: {floor}")

    # Second part
    basement_entry = find_basement_entry(instructions)
    print(f"Santa is entering basement at: {basement_entry}")
