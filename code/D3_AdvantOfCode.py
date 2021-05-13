directions = []
with open('.//input//input_d3.txt') as data:
    for line in data:
        for char in line:
            directions.append(char)

visited = set()
santaX, santaY = 0, 0
roboX, roboY = 0, 0

visited.add((0, 0)) # the initial starting position
turn = 1

for direction in directions:
    if direction == "^":
        if turn % 2 != 0:
            santaY += 1
            visited.add((santaX, santaY))
        else:
            roboY += 1
            visited.add((roboX, roboY))
    elif direction == "v":
        if turn % 2 != 0:
            santaY -= 1
            visited.add((santaX, santaY))
        else:
            roboY -= 1
            visited.add((roboX, roboY))
    elif direction == ">":
        if turn % 2 != 0:
            santaX += 1
            visited.add((santaX, santaY))
        else:
            roboX += 1
            visited.add((roboX, roboY))
    elif direction == "<":
        if turn % 2 != 0:
            santaX -= 1
            visited.add((santaX, santaY))
        else:
            roboX -= 1
            visited.add((roboX, roboY))
    turn += 1

print(len(visited))