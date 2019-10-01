"""
Constantly get available driving exam times from "Maanteeamet" e-service website
and continue to compare these times against each other until a closer comes up,
at which point start playing a alert(requires audio output).
Meant to be left running undisturbed for a long periods.
"""
from pynput.mouse import Button, Controller as Mouse_controller
from pynput.keyboard import Key, Controller as Key_controller
from time import sleep
import time
import winsound
import pyperclip
import re
import pyttsx3

time_unit = 8       # Determines webscraping speed
old_reservations = []
new_reservations = []
mouse = Mouse_controller()
keyboard = Key_controller()


def alert():
    """Play alert sound."""
    for _ in range(25):
        winsound.PlaySound("sound2.wav", winsound.SND_ASYNC)
        speak("Time  available.")
        sleep(2)
    # Todo! Send email message!
    exit()


def go_to_desktop():
    """Go to desktop."""
    keyboard.press(Key.cmd)
    keyboard.press("d")
    keyboard.release("d")
    keyboard.release(Key.cmd)


def copy_page_source():
    """Copy website html into clipboard."""
    mouse.position = (200, 200)
    mouse.click(Button.right)
    sleep(0.1 * time_unit)
    mouse.move(100, 190)  # mouse.position = (300, 390)
    mouse.click(Button.left)
    sleep(0.3 * time_unit)
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    sleep(0.3 * time_unit)
    keyboard.press("c")
    keyboard.release("c")
    keyboard.release(Key.ctrl)
    sleep(0.1 * time_unit)
    close_browser_tab()
    sleep(0.3 * time_unit)
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)

# Unused
def open_new_schedule_tab():
    """Opens a new tab with calender popup."""
    mouse.position = (400, 650)
    mouse.click(Button.left)
    sleep(0.3 * time_unit)
    mouse.click(Button.right)
    mouse.move(10, 19)
    sleep(0.1 * time_unit)
    mouse.click(Button.left)
    sleep(0.1 * time_unit)

# Unused
def inspect_new_tab():
    mouse.position = (260, 40)   # new tab location
    sleep(0.1 * time_unit)
    mouse.click(Button.left)
    sleep(0.1 * time_unit)
    mouse.position = (710, 350)  # popup top side
    sleep(0.1 * time_unit)
    mouse.click(Button.right)
    sleep(0.3 * time_unit)
    keyboard.press("q")
    sleep(0.1 * time_unit)
    keyboard.release("q")
    sleep(0.3 * time_unit)

    mouse.position = (400, 820)  # correct html line when inspection bar begins on y = 670, 12 rows
    mouse.click(Button.right)
    sleep(0.1 * time_unit)
    mouse.move(80, -80)            # copy button
    # mouse.position = (480, 780)  # copy button
    sleep(0.1 * time_unit)
    mouse.move(190, 0)             # copy inner HTML
    # mouse.position = (670, 780)  # copy inner HTML
    sleep(0.1 * time_unit)
    mouse.click(Button.left)
    sleep(0.1 * time_unit)


def close_browser_tab():
    """Closes active browser tab using windows shortcut."""
    keyboard.press(Key.ctrl)
    keyboard.press("w")
    keyboard.release("w")
    keyboard.release(Key.ctrl)
    sleep(1)


class AvailableReservation:
    """Turn available times into objects."""

    def __init__(self, date, clock_time, place):
        self.date = date
        self.time = clock_time
        self.place = place

    def hold_old_reservation(self):
        old_reservations.append(self)

    def hold_new_reservation(self):
        new_reservations.append(self)

    def __repr__(self):
        return self.date + ", " + self.time + ", " + self.place


def clipboard_pattern_finder(reservation_list_ref):
    """
    Find regex matches from clipboard.
    Matches have 3 capturing groups.
    1. Date
    2. Time
    3. Place

    Example1:
    1. 16.12.2019
    2. 09:00
    3. Tartu

    Turn times into objects and put them into the correct list.
    Exit process when there are no matches.

    :var reservation_list_ref - boolean value. Refers to lists old_reservations and new_reservations.
    False on first run old_reservations, elements will be saved for later comparison.
    True for new_reservations. Will be actively used on every subsequent cycle.
    """
    input_string = str(pyperclip.paste())
    regex = "(\d{2}\.\d{2}\.\d{4})(?:[^[0-9]+)(\d{2}\:\d{2})(?:[^[A-Z]+)([^ ]+)"

    no_matches = True
    for match in re.finditer(regex, input_string):
        no_matches = False
        time_object = AvailableReservation(match.group(1), match.group(2), match.group(3))
        if not reservation_list_ref:
            AvailableReservation.hold_old_reservation(time_object)
        else:
            AvailableReservation.hold_new_reservation(time_object)
    if no_matches:
        print("No matches")
        exit()


def compare_lists():
    if str(old_reservations) != str(new_reservations):
        if len(new_reservations) != len(old_reservations):
            speak("Lists are different size!")
            print(old_reservations)
            print(new_reservations)
            if len(new_reservations) < len(old_reservations):
                n_deleted_old_reservations = 0
                for i in range(len(new_reservations)):
                    if new_reservations[i] != old_reservations[i - n_deleted_old_reservations]:
                        del old_reservations[i - n_deleted_old_reservations]
                        n_deleted_old_reservations += 1
                assert str(new_reservations) == str(old_reservations)
                print("Lists are equal.")
                return
            elif len(new_reservations) > len(old_reservations):
                print("New Times have been inserted.")
                alert()
            print("Lists are equal.")
        for i in range(len(new_reservations)):
            old_date = time.strptime(new_reservations[i].date, "%d.%m.%Y")
            new_date = time.strptime(old_reservations[i].date, "%d.%m.%Y")
            if new_date == old_date:
                continue
            if new_date > old_date:
                old_reservations[i].date = new_reservations[i].date
            else:
                closer_time_found(new_reservations[i])
    else:
        print("Lists are equal.")
        return


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()


def closer_time_found(closer_time):
    print("Old times:")
    print(old_reservations)
    print("New times:")
    print(new_reservations)
    print("New time:")
    print(closer_time)
    alert()


if __name__ == '__main__':

    # mouse.position = (300, 390)
    # speak("30 seconds")
    # alert()

    # Data for debugging
    # [16.12.2019, 09:00, Tartu, 17.12.2019, 15:45, Kuressaare, 18.12.2019, 09:00, Viljandi, 18.12.2019, 11:30, Pärnu, 27.12.2019, 13:15, Võru, 02.01.2020, 14:30, Rakvere, 03.01.2020, 14:30, Tallinn, 08.01.2020, 09:00, Paide, 09.01.2020, 13:15, Haapsalu, 15.01.2020, 11:30, Narva, 16.01.2020, 10:15, Jõhvi]
    # [16.12.2019, 14:30, Tartu, 17.12.2019, 10:15, Kuressaare, 18.12.2019, 13:15, Viljandi, 20.12.2019, 09:00, Pärnu, 27.12.2019, 09:00, Võru, 06.01.2020, 11:30, Rakvere, 08.01.2020, 09:00, Tallinn, 09.01.2020, 11:30, Haapsalu, 13.01.2020, 09:00, Paide, 15.01.2020, 09:00, Narva, 17.01.2020, 11:30, Jõhvi]
    #

    if True:

        go_to_desktop()
        sleep(4)  # time for pulling out required website

        copy_page_source()
        clipboard_pattern_finder(False)

        while True:
            copy_page_source()
            clipboard_pattern_finder(True)
            compare_lists()

            print(time.strftime("%H:%M:%S", time.localtime()))
            print(new_reservations)
            print(old_reservations)
            print()

            new_reservations.clear()
            speak("30 seconds")
            sleep(25)
            speak("5 seconds")
            sleep(5)
