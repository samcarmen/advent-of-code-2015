def paper_required(l, w, h):
    sides = [l * w, w * h, h * l]
    surface_area = sum([2 * s for s in sides])
    return surface_area + min(sides)


def ribbon_required(l, w, h):
    sides = sorted([l, w, h])
    return 2 * (sides[0] + sides[1]) + l * w * h


def total_paper_required(box_list):
    total_paper = 0
    total_ribbon = 0
    for box in box_list:
        l, w, h = map(int, box.split("x"))
        total_paper += paper_required(l, w, h)
        total_ribbon += ribbon_required(l, w, h)
    return total_paper, total_ribbon


if __name__ == "__main__":
    with open("./input/D2.txt") as file:
        dimensions = file.readlines()

    print(f"Total paper and ribbon: {total_paper_required(dimensions)}")
