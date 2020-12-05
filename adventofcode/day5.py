def seat_number(seat_string):
    # determine row
    span = 128
    upper = 127
    lower = 0
    for character in seat_string[:7]:
        span //= 2
        if character == "F":
            upper -= span
        elif character == "B":
            lower += span
    row = lower

    # determine column
    span = 8
    upper = 7
    lower = 0
    for character in seat_string[7:]:
        span //= 2
        if character == "L":
            upper -= span
        elif character == "R":
            lower += span
    column = lower

    return (row, column)


def seat_id(row, column):
    return row * 8 + column


def empty_seats(boarding_passes):
    occupied = set([seat_id(*seat_number(seat)) for seat in boarding_passes])
    every = set(
        [seat_id(row, column) for row in range(128) for column in range(8)]
    )

    return (every - occupied)


def my_seat(boarding_passes):
    seats = empty_seats(boarding_passes)
    for seat_number in list(seats):
        if (seat_number + 1) not in seats and (seat_number - 1) not in seats:
            return seat_number
