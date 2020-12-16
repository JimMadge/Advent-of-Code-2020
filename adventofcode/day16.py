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


def valid(ticket, rules):
    for value in ticket:
        if not any(rule.check(value) for rule in rules):
            return False

    return True


def discard_invalid(tickets, rules):
    valid_tickets = []
    for ticket in tickets:
        if valid(ticket, rules):
            valid_tickets.append(ticket)

    return valid_tickets


def match_rule_and_column(tickets, column, rule):
    values = [ticket[column] for ticket in tickets]
    return all(rule.check(value) for value in values)


def part2(rules, tickets, my_ticket):
    tickets = discard_invalid(tickets, rules)
    n_columns = len(tickets[0])
    # Find which columns may match which rules
    matches = [
        (rule, [column for column in range(n_columns)
                if match_rule_and_column(tickets, column, rule)])
        for rule in rules
    ]

    confirmed = []
    while len(confirmed) < n_columns:
        # Find a rule which has only one possible column
        for rule, columns in matches:
            if len(columns) == 1:
                found = columns[0]
                confirmed.append((rule, found))
        # Remove that column as a possibility from all rules
        for rule, columns in matches:
            if found in columns:
                columns.remove(found)

    result = 1
    for rule, column in confirmed:
        if rule.name.startswith("departure"):
            result *= my_ticket[column]
    return result
