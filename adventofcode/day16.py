import re


parse_rule = re.compile(r"(\d+)-(\d+) or (\d+)-(\d+)")


class Rule(object):
    def __init__(self, name, rule_string):
        self.name = name
        (self.lowera, self.uppera,
         self.lowerb, self.upperb) = (int(elem) for elem in
                                      parse_rule.match(rule_string).groups())

    def check(self, value):
        return (self.lowera <= value <= self.uppera
                or self.lowerb <= value <= self.upperb)


def create_rule(string):
    return Rule(*string.split(": "))


def parse_ticket(string):
    return [int(elem) for elem in string.split(",")]


def completely_invalid(rules, tickets):
    invalid = []
    for ticket in tickets:
        for value in ticket:
            if not any(rule.check(value) for rule in rules):
                invalid.append(value)

    return invalid
