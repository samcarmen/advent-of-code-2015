def count_characters_in_file(filename):
    code_count = 0  # Number of characters in code representation
    memory_count = 0  # Number of characters in memory

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()  # Remove whitespace
            code_count += len(line)

            # Strip the double quotes at the beginning and end
            line = line[1:-1]

            i = 0
            while i < len(line):
                if line[i] == "\\":
                    if line[i + 1] in ('"', "\\"):
                        memory_count += 1
                        i += 2  # Skip the escape and the escaped character
                    elif line[i + 1] == "x":
                        memory_count += 1
                        i += 4  # Skip \x and the two hexadecimal digits
                else:
                    memory_count += 1
                    i += 1  # Regular character

    return code_count - memory_count


if __name__ == "__main__":
    filename = "./input/D8.txt"
    result = count_characters_in_file(filename)
    print("Difference between code characters and memory characters:", result)
