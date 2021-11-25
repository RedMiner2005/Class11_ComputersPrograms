from datetime import date, datetime
import re
import zipfile
import os
from json import load

# import pyperclip


zipapp = False


def import_roll_list():
    if zipapp:
        with zipfile.ZipFile(os.path.dirname(__file__)) as z:
            with z.open("namelist.json") as f:
                name_list_json = load(f)
    name_list_json = load(open("namelist.json"))
    name_list = list(name_list_json["list"])
    total = len(name_list)
    return list(range(1, total + 1)), total, name_list


def process_messages(messages: str) -> list:
    pattern = r'\[(?P<time>\d+\:\d+), (?P<date>\d+\/\d+\/\d+)\] (?P<phone_number_1>.+):[ +](?P<name>.+)[\n\r\s]+(?P<roll_number>\d+[\n\r\s])'
    return re.split(pattern, messages)


def extract_absent(messages: str, roll_list: list, total: int) -> list:
    matches = process_messages(messages)
    entry = []
    with open("_QuickerAttendanceCheckerLogs/log{}.txt".format(date.today()), "a") as file:
        rejected = False
        file.write("START " + str(datetime.now()) + "\n")
        for element in matches[1:]:
            if element.strip() == "" or element.startswith("\\n") or element.startswith("["):
                roll = entry[-1]
                if not (0 < (roll := int(roll)) <= total):
                    print("Roll number does not fall within the range of 1 ->", total, ".\n")
                    continue
                if roll not in roll_list:
                    print("Already marked present.\n")
                    continue

                if not rejected:
                    roll_list.remove(roll)
                file.write(",".join(entry) + (" REJECTED" if rejected else ""))
                entry = []
                rejected = False
            else:
                if entry == [] and not element[0].isdigit():
                    continue
                if "Ma'am" in element:
                    rejected = True
                entry.append(element)
        file.write("END\n")
    return roll_list


def main():
    all_messages = ""
    roll_no_list, total_list, namelist = import_roll_list()

    while True:
        string = input()
        if string == "stop":
            break
        all_messages += string + "\n"

    absent = extract_absent(all_messages, roll_no_list, total_list)
    if len(absent) == 0:
        output = "All have marked attendance in WhatsApp."
    else:
        if len(absent) == 1:
            output = "Roll number {} has not marked attendance in WhatsApp.".format(
                    absent[0] + "-" + namelist[absent[0] - 1]
                )
        else:
            output = "Roll numbers {} have not marked attendance in WhatsApp.".format(
                        " and ".join(", ".join((str(i) + "-" + namelist[i - 1]) for i in absent).rsplit(", ", 1)
                    )
                )
    # pyperclip.copy(output)
    print("\n" + output + "(Copied)")


if __name__ == '__main__':
    print("^-----------------------------------------------------^")
    print("^   Q U I C K E R   A B S E N T E E   C H E C K E R   ^")
    print("^ Almost fully automatic edition - v1.0 - By Pratyush ^")
    print("^-----------------------------------------------------^")
    print("Enter the copied WhatsApp messages (When you are done, type 'stop'):\n")
    main()
    input("\nPress enter to exit.")
