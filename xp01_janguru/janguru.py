"""Jängurud lähevad loomaaeda."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Arvutab jängurude kohtumisasukoha."""
    max_sleep1 = sleep1
    max_sleep2 = sleep2
    run_time = 100000
    # the higher the better, but takes more time
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
        if sleep1 > 0:
            sleep1 = sleep1 - 1
        if sleep2 > 0:
            sleep2 = sleep2 - 1

    if run_time == 0:
        return -1
        # don't meet

    else:
        return pos1
        # meet


# pos1 = int(input("pos1:"))
# jump_distance1 = int(input("jump_distance1:"))
# sleep1 = int(input("sleep1:"))
# pos2 = int(input("pos2:"))
# jump_distance2 = int(input("jump_distance2:"))
# sleep2 = int(input("sleep2:"))

# meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2)
