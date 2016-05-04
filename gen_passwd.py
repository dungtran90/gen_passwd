#!/usr/bin/env python

"""
    Create random pasword with:
        + least one lowercase
        + least one uppercase
        + least one digit
        + least one punctuation
        + length = 16
"""

import random
import string


def gen_passwd(passwd_length=16):
    """
    Create password with default length = 16
    """

    result = ""
    all_char_groups = [
        string.ascii_lowercase, string.ascii_uppercase,
        string.digits, string.punctuation]
    for char_group in all_char_groups:
        result += random.choice(char_group)
    result += "".join(random.sample(
        "".join(all_char_groups),
        passwd_length - len(result)))
    return "".join(random.sample(result, len(result)))


if __name__ == "__main__":
    print gen_passwd()
