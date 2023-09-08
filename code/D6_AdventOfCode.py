def parse_instruction(instruction):
    """Parses the instruction and returns the action and coordinates."""
    if instruction.startswith("turn on"):
        action = "on"
        coords = instruction[8:].split(" through ")
    elif instruction.startswith("turn off"):
        action = "off"
        coords = instruction[9:].split(" through ")
    elif instruction.startswith("toggle"):
        action = "toggle"
        coords = instruction[7:].split(" through ")
    else:
        raise ValueError("Invalid instruction")

    start_x, start_y = map(int, coords[0].split(","))
    end_x, end_y = map(int, coords[1].split(","))

    return action, start_x, start_y, end_x, end_y


def execute_instruction(grid, instruction):
    """Executes the instruction on the given grid."""
    action, start_x, start_y, end_x, end_y = parse_instruction(instruction)

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "on":
                grid[x][y] = 1
            elif action == "off":
                grid[x][y] = 0
            elif action == "toggle":
                grid[x][y] ^= 1


def main(instructions):
    # Initialize a 1000x1000 grid with all lights off
    grid = [[0] * 1000 for _ in range(1000)]

    with open('./input/D6_Input.txt') as data:
        for instruction in data:
            instructions.append(instruction)

    print(instructions)
    # Execute each instruction
    for instruction in instructions:
        execute_instruction(grid, instruction)

    # Count the lights that are on
    return sum(sum(row) for row in grid)


print(main([]))  # Expected output: 1001996
