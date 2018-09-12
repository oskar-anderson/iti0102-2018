"""Jängurud lähevad loomaaeda."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Arvutab jängurude kohtumisasukoha."""
    max_sleep1 = sleep1
    max_sleep2 = sleep2
    run_time = 10000000
    # The higher the better, but takes more time -100000 has gotten best results
    starting_pos1 = pos1
    starting_pos2 = pos2

    pos1 += jump_distance1
    pos2 += jump_distance2
    # First jump

    while pos1 != pos2 and run_time > 0:
        run_time = run_time - 1
        if run_time == 1 and abs(pos1 - pos2) < abs(starting_pos1 - starting_pos2):
            run_time = 1000000
            # resets run_time if the rabbits have gotten closure since the start

        # Jumping
        if sleep1 == 0:
            pos1 += jump_distance1
            sleep1 = max_sleep1
        if sleep2 == 0:
            pos2 += jump_distance2
            sleep2 = max_sleep2

        # Sleep pass turn
        if sleep1 > 0 and sleep2 > 0:
            sleep1_simultaneous_reduction = sleep1
            # allows to reduce both sleep timers simultaneously.
            sleep1 = sleep1 - min(sleep1, sleep2)
            sleep2 = sleep2 - min(sleep1_simultaneous_reduction, sleep2)

    if run_time == 0:
        return -1
        # Do not meet

    else:
        return pos1
        # Meet--> pos1 == pos2


# print(meet_me(1, 2, 1, 2, 1, 1))
# print(meet_me(1, 2, 3, 4, 5, 5))
# print(meet_me(10, 7, 7, 5, 8, 6))
# print(meet_me(100, 7, 4, 300, 8, 6))
# print(meet_me(1, 7, 1, 15, 5, 1))
# print(meet_me(0, 1, 1, 1, 1, 1))

# meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2)
