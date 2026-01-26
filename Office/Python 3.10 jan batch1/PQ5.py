def max_new_people(seat_row):
    """
    Calculate the maximum number of new people who can be seated
    maintaining at least 2 empty seats gap.
    """
    total_seats = len(seat_row)
    new_people_count = 0

    for seat_index in range(total_seats):
        if seat_row[seat_index] == 0:
            # Check left 2 seats
            left_clear = (seat_index == 0 or seat_row[seat_index - 1] == 0) and \
                         (seat_index <= 1 or seat_row[seat_index - 2] == 0)

            # Check right 2 seats
            right_clear = (seat_index == total_seats - 1 or seat_row[seat_index + 1] == 0) and \
                          (seat_index >= total_seats - 2 or seat_row[seat_index + 2] == 0)

            # If both sides clear, seat a new person
            if left_clear and right_clear:
                seat_row[seat_index] = 1
                new_people_count += 1

    return new_people_count

seats = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
print(max_new_people(seats))  # Output: 2

seats = [0, 0, 0, 0]
print(max_new_people(seats))  # Output: 2
