def num_houses(directions):
    # Initialize Santa's starting position and the set of visited houses
    x, y = 0, 0
    visited_houses = {(x, y)}

    # Map of directions to their corresponding coordinate changes
    moves = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

    for direction in directions:
        dx, dy = moves[direction]
        x += dx
        y += dy
        visited_houses.add((x, y))

    return len(visited_houses)


def num_houses_with_robo(directions):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited_houses = {(santa_x, santa_y)}

    moves = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for idx, direction in enumerate(directions):
        dx, dy = moves[direction]
        if idx % 2 == 0:
            santa_x += dx
            santa_y += dy
            visited_houses.add((santa_x, santa_y))
        else:
            robo_x += dx
            robo_y += dy
            visited_houses.add((robo_x, robo_y))

    return len(visited_houses)


if __name__ == "__main__":
    with open("./input/D3.txt", "r") as file:
        directions = file.readline()

    print(num_houses(directions))
    print(num_houses_with_robo(directions))
