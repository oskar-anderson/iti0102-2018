"""Jängurud lähevad loomaaeda."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

    first_jump = 1
    permanent_sleep1 = sleep1
    permanent_sleep2 = sleep2
    run_times = 100000
    # the higher the better, but takes more time

    while pos1 != pos2 and run_times > 0:
        run_times = run_times - 1

        # First jump
        if first_jump == 1:
            pos1 = pos1 + jump_distance1
            pos2 = pos2 + jump_distance2
            first_jump = 0

        # Jumping
        if sleep1 == 0:
            pos1 = pos1 + jump_distance1
            sleep1 = permanent_sleep1
        if sleep2 == 0:
            pos2 = pos2 + jump_distance2
            sleep2 = permanent_sleep2

        # Sleep pass turn
        if sleep1 > 0:
            sleep1 = sleep1 - 1
        if sleep2 > 0:
            sleep2 = sleep2 - 1

    if run_times == 0:
        print("-1")
        # don't meet

    else:
        print(pos1)
        # meet
