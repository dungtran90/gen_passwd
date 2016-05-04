import string
import random

PASSWD_LENGTH = 16


def gen_passwd():
    result = ""
    all_chars = [
        string.ascii_lowercase, string.ascii_uppercase,
        string.digits, string.punctuation]
    for s in all_chars:
        result += random.choice(s)
    result += ("".join(random.sample("".join(all_chars), PASSWD_LENGTH - len(result))))
    return "".join(random.sample(result, len(result)))


if __name__ == "__main__":

    print gen_passwd()
