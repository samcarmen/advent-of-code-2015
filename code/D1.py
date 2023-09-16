current_floor = 0
position = 1

with open(".//input//D1_Input.txt") as data:
    for line in data:
        for ele in line:
            if ele == "(":
                current_floor += 1
                if current_floor < 0:
                    break
                position += 1
            else:
                current_floor -= 1
                if current_floor < 0:
                    break
                position += 1
print(position)
