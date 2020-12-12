import re

regex = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse_line(line):
    match = re.match(regex, line)
    if match:
        return (int(match[1]), int(match[2]), match[3], match[4])
    return None


def valid_password1(minimum, maximum, character, password):
    return minimum <= password.count(character) <= maximum


def valid_password2(first_pos, second_pos, character, password):
    a = password[first_pos-1] == character
    b = password[second_pos-1] == character

    return (a and not b) or (b and not a)


def count_valid_passwords(validator, lines):
    return sum([validator(*parse_line(line)) for line in lines])
