import re

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


def process_passports(passports):
    # Split each key:value pair by ":" and create a dictionary for each
    # passport
    return [
        dict(item.split(":") for item in passport.split())
        for passport in passports.split("\n\n")
    ]


def valid_passport(passport):
    return all([key in passport.keys() for key in required_fields])


def count_valid_passports(passports):
    return sum(
        [valid_passport(passport) for passport in passports]
    )


height_range = {
    "cm": (150, 193),
    "in": (59, 76)
}

hair_colour = re.compile(r"#[0-9A-Fa-f]{6}")

eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

passport_number = re.compile(r"\d{9}")


def valid_passport2(passport):
    if not all([key in passport.keys() for key in required_fields]):
        return False

    if not 1920 <= int(passport["byr"]) <= 2002:
        return False

    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False

    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False

    if (height_unit := passport["hgt"][-2:]) in ["cm", "in"]:
        if not (height_range[height_unit][0] <= int(passport["hgt"][:-2])
                <= height_range[height_unit][1]):
            return False
    else:
        return False

    if not hair_colour.fullmatch(passport["hcl"]):
        return False

    if not passport["ecl"] in eye_colours:
        return False

    if not passport_number.fullmatch(passport["pid"]):
        return False

    return True


def count_valid_passports2(passports):
    return sum(
        [valid_passport2(passport) for passport in passports]
    )
