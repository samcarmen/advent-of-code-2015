input_list, number, total = [], [], 0

with open('./input/D2_Input.txt') as file_input:
    for each in file_input:
        each = each.rstrip().split('x')
        converted = [int(i) for i in each]
        [l, w, h] = sorted(converted)
        subtotal = 2*l*w + 2*w*h + 2*l*h + l*w
        total += subtotal

####### Ribbon #######
with open('.//input//D2_Input.txt') as file_input:
    total = 0
    for each in file_input:
        each = each.rstrip().split('x')
        converted = [int(i) for i in each]
        [l, w, h] = sorted(converted)
        subtotal = l + l + w + w + (l*w*h)
        total += subtotal

print(total)