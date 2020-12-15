def memory_game(starting_numbers, end_turn=2020):
    # Create log of numbers when they were last said and if this is the first
    # time they have been said
    numbers = dict()

    # Initialise using starting numbers except for the last
    numbers = {number: turn
               for turn, number in enumerate(starting_numbers[:-1], start=1)}

    # Play the game
    last_number = starting_numbers[-1]
    for turn in range(len(starting_numbers)+1, end_turn+1):
        if last_number in numbers.keys():
            # Current number is difference between last turn and previous time
            # last number was said
            current_number = (turn - 1) - numbers[last_number]
        else:
            # First time number was said, current number is 0
            current_number = 0

        numbers[last_number] = turn - 1
        last_number = current_number

    return current_number
