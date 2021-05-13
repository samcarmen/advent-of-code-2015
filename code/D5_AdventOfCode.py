######### Nice String Part 1 #########
def check_vowels(string):
    vowel = ['a', 'e', 'i', 'o', 'u']           
    vowel_num = 0

    for char in string:
        if char in vowel:
            vowel_num += 1

    if vowel_num >= 3:
        return True
    return False


def check_appear_twice(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False


def check_bad_strings(string):
    bad_letters = ['ab', 'cd', 'pq', 'xy'] 
    for bad in bad_letters:
        if bad in string:
            return False
    return True


######### Nice String Part 2 #########
def check_overlaps(string):
    for i in range(len(string)-1):
        pair = string[i] + string[i+1]
        for j in range(i+2, len(string)-1):
            if pair == string[j] + string[j+1]:
                return True
    return False

def check_repeat_between_character(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True   

if __name__ == "__main__":
    nice_string = 0
    with open('.//input//D5_Input.txt') as data: 
        for line in data:
            string = line.strip()

        # string = 'qjhvhtzxzqqjkmpb'
            if check_overlaps(string) and check_repeat_between_character(string):
                nice_string += 1
    print(nice_string)

