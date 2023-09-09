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


def adjust_lights_brightness(grid, instructions):
    for instruction in instructions:
        action, start_x, start_y, end_x, end_y = parse_instruction(instruction)
        
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == "turn on":
                    grid[x][y] += 1
                elif action == "turn off":
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif action == "toggle":
                    grid[x][y] += 2
    return grid


def total_brightness_after_instructions(instructions, grid_size=1000):
    # Initialize the grid with a brightness of 0 for each light
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Adjust the lights' brightness based on the instructions
    grid = adjust_lights_brightness(grid, instructions)
    
    # Calculate the total brightness
    total_brightness = sum(sum(row) for row in grid)
    
    return total_brightness


def main(instructions):
    # Initialize a 1000x1000 grid with all lights off
    grid = [[0] * 1000 for _ in range(1000)]

    with open('./input/D6.txt') as data:
        for instruction in data:
            instructions.append(instruction)

    print(instructions)
    # Execute each instruction
    for instruction in instructions:
        execute_instruction(grid, instruction)

    result = total_brightness_after_instructions(instructions)
    return result
    # Count the lights that are on
    return sum(sum(row) for row in grid)


print(main([]))  # Expected output: 1001996
