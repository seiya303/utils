import random
import string

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    print("Random alphanumeric String is:", result_str)

if __name__ == "__main__":
    lengths = [8, 4, 4, 4, 12]
    for length in lengths:
        get_random_alphanumeric_string(length)