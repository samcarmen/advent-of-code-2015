import hashlib


def find_lowest_number_for_md5(secret_key, prefix="00000"):
    num = 0
    while True:
        data = f"{secret_key}{num}".encode()
        result = hashlib.md5(data).hexdigest()
        if result.startswith(prefix):
            return num
        num += 1


if __name__ == "__main__":
    secret_key = "ckczppom"

    # Part 1
    print(find_lowest_number_for_md5(secret_key))

    # Part 2
    print(find_lowest_number_for_md5(secret_key, "000000"))
