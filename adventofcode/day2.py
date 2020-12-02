import re

regex = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse_line(line):
    match = re.match(regex, line)
    if match:
        return (int(match[1]), int(match[2]), match[3], match[4])
    return None


def valid_password(minimum, maximum, character, password):
    return minimum <= password.count(character) <= maximum


def count_valid_passwords(lines):
    return sum([valid_password(*parse_line(line)) for line in lines])
