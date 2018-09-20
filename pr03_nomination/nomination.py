"""Nominee setup system."""
import time


def ask_name():
    """Ask the user's name."""
    while True:
        name = input("What is your full name, dear fellow?").strip()

        is_spaced = " " in name
        is_alpha = name.replace(" ", "").replace("-", "").isalpha()
        # is_alpha = name.find(" ") != -1
        if name.istitle() and is_spaced and is_alpha:
            return name
        else:
            print("Sorry, try again.")


def progress_bar(process_name, seconds):
    """Show the progressbar."""
    cycle_time = seconds / 20

    chr_limit = 25

    if len(process_name) > chr_limit - 2:
        process_name = f"{process_name[:20]}..."

    for i in range(21):
        print(f"\r[{'|' * i:-<20}] | Process: {process_name!r} {0.05 * i:4.0%}", end='')
        time.sleep(cycle_time)

    print()


def print_ok():
    """Print final state."""
    print("Nominee listed.")


if __name__ == "__main__":
    ask_name()
    progress_bar("Setting up the nominee", 5)
    print_ok()
    # progress_bar("abcdef" * 10, 3)
