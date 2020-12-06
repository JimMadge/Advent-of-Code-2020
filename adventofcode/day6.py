def filter_affirmative(answers):
    """Create a set of affirmative answers"""
    return set(answers.replace("\n", ""))


def filter_all_affirmative(group_answers):
    """Create a set of answers which are affirmative for all group members"""
    individual_answers = [
        filter_affirmative(answers) for answers in group_answers.split("\n")
    ]
    return set.intersection(*individual_answers)


def count_any_affirmative(groups):
    return sum(map(len, map(filter_affirmative, groups)))


def count_all_affirmative(groups):
    return sum(map(len, map(filter_all_affirmative, groups)))
