import hashlib

key = 'bgvyzdsv'
hexa = hashlib.md5(key.encode())
num = 0

while hexa.hexdigest()[0:6] != '000000':
    new_key = key + str(num)
    hexa = hashlib.md5(new_key.encode())
    num += 1

print(num-1)
