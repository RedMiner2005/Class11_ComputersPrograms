"""namelist.json is not included in the repository for obvious reasons.
Just make it in the following format:
{
    "list": [
        "Someone",
        "Noone",
        "Anyone",
    ]
}"""


from json import load


print("^---------------------------------------------^")
print("^ Q U I C K   A B S E N T E E   C H E C K E R ^")
print("^ Semi-automatic edition - v1.0 - By Pratyush ^")
print("^---------------------------------------------^")

print("\nKeep entering roll numbers, and end your input by typing: stop")

namelist_json = load((file := open("namelist.json")))
namelist = list(namelist_json["list"])
total = len(namelist)
rolllist = list(range(1, total + 1))

while True:
    if not (roll := input().strip()).isdigit():
        if roll == "stop":
            break
        elif roll == "":
            continue
        print("Invalid roll number.\n")
        continue
    if not (0 < (roll := int(roll)) <= total):
        print("Roll number does not fall within the range of 1 ->", total, ".\n")
        continue
    if roll not in rolllist:
        print("Already marked present.\n")
        continue
    rolllist.remove(roll)

if len(rolllist) == 0:
    print("\nAll have marked attendance in WhatsApp.")
else:
    print("\nRoll number {} {} not marked attendance in WhatsApp.".format(", ".join((str(i) + "-" + namelist[i - 1]) for i in rolllist), "have" if len(rolllist) > 1 else "has"))
input()
    