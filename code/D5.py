def vowel_counter(string):
    vowel = "aeiou"
    vowel_counter = 0
    for letter in list(string):
        if letter in vowel:
            vowel_counter += 1
    return vowel_counter


def letter_appears_twice(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


def has_bad_strings(string):
    bad_letters = ["ab", "cd", "pq", "xy"]
    for letter in bad_letters:
        if letter in string:
            return True
    return False


def check_overlaps(string):
    for i in range(len(string) - 1):
        pair = string[i] + string[i + 1]
        for j in range(i + 2, len(string) - 1):
            if pair == string[j] + string[j + 1]:
                return True
    return False


def check_repeat_between_character(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True


if __name__ == "__main__":
    with open("./input/D5.txt", "r") as file:
        strings = file.readlines()

    # Part 1
    nice_string = 0
    for string in strings:
        if not has_bad_strings(string):
            if vowel_counter(string) >= 3 and letter_appears_twice(string):
                nice_string += 1
    print(nice_string)

    # Part 2
    nice_string = 0
    for string in strings:
        if check_overlaps(string) and check_repeat_between_character(string):
            nice_string += 1
    print(nice_string)
