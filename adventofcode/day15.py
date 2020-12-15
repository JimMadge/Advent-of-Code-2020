def memory_game(starting_numbers, end_turn=2020):
    # Create log of numbers when they were last said and if this is the first
    # time they have been said
    numbers = dict()

    # Initialise using starting numbers
    for turn, number in enumerate(starting_numbers, start=1):
        numbers[number] = ([turn], True)

    # Play the game
    turn += 1
    last_number = starting_numbers[-1]
    for turn in range(turn, end_turn+1):
        turns_said, first_occurance = numbers[last_number]

        if first_occurance:
            # If this is the first occurrence, say 0
            current_number = 0
        else:
            # Otherwise say the difference between the last turn and the time
            # the number was previously said (not including the last turn!)
            # current_number = turns_said[-1] - turns_said[-2]
            current_number = (turn-1) - turns_said[-2]

        if current_number in numbers.keys():
            # Update an existing occurance
            numbers[current_number] = (numbers[current_number][0]+[turn],
                                       False)
        else:
            # Add a new occurrence to the record
            numbers[current_number] = ([turn], True)

        last_number = current_number

    return current_number
