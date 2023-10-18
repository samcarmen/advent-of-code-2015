def apply_instruction(instruction):
    parts = instruction.split()
    if parts[0] == "turn":
        operation = parts[1]
        start_x, start_y = map(int, parts[2].split(","))
        end_x, end_y = map(int, parts[4].split(","))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if operation == "on":
                    grid[x][y] += 1
                elif operation == "off":
                    grid[x][y] = max(0, grid[x][y] - 1)
    elif parts[0] == "toggle":
        start_x, start_y = map(int, parts[1].split(","))
        end_x, end_y = map(int, parts[3].split(","))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                grid[x][y] += 2


if __name__ == "__main__":
    # Initialize a 1000x1000 grid of lights with brightness set to 0
    grid = [[0] * 1000 for _ in range(1000)]

    with open("./input/D6.txt", "r") as file:
        instructions = file.read().splitlines()
        for instruction in instructions:
            apply_instruction(instruction)

    # Calculate the total brightness of all lights combined
    total_brightness = sum(sum(row) for row in grid)

    print("Total brightness of all lights combined:", total_brightness)
