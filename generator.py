import random
import string

def generate_password(length=12, digits=True, symbols=True):
    letters = string.ascii_letters
    digits_set = string.digits if digits else ""
    symbols_set = "!@#$%^&*()_+-=" if symbols else ""

    all_chars = letters + digits_set + symbols_set

    if not all_chars:
        raise ValueError("No characters selected for password generation.")

    return "".join(random.choice(all_chars) for _ in range(length))


def generate_multiple(count, length=12, digits=True, symbols=True):
    return [
        generate_password(length, digits, symbols)
        for _ in range(count)
    ]
