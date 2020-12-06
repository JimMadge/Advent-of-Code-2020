def filter_affirmative(answers):
    return set(answers.replace("\n", ""))


def filter_all_affirmative(group_answers):
    individual_answers = [
        set(answers) for answers in group_answers.split("\n")
    ]
    return set.intersection(*individual_answers)


def groups_affirmative(group_answers):
    return [
        filter_affirmative(answers) for answers in group_answers.split("\n\n")
    ]


def groups_all_affirmative(group_answers):
    return [
        filter_all_affirmative(answers)
        for answers in group_answers.split("\n\n")
    ]


def count_groups_affirmative(group_answers):
    return [
        len(affirmative) for affirmative in groups_affirmative(group_answers)
    ]


def count_groups_all_affirmative(group_answers):
    return [
        len(affirmative)
        for affirmative in groups_all_affirmative(group_answers)
    ]
