import string
import random


def create_code():
    letters = string.ascii_letters+string.digits
    letters = list(letters)
    random.shuffle(letters)
    return "".join(letters[:6])



