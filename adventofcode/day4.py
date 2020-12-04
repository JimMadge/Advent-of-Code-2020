required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]


def valid_passport(passport):
    return all([key in passport for key in required_fields])


def count_valid_passports(passports):
    return sum(
        [valid_passport(passport) for passport in passports.split("\n\n")]
    )
