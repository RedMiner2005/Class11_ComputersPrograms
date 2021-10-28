# Practical Implementation - 4 : 22 Oct 2021
# Order of digits and alphabets have been exchanged so that v2 can be matched by v1 and v2_2


def v1(line: str):
    """Adds output of is.. directly to each, alphacount
    is calculated by adding lowercount and uppercount."""

    lowercount = uppercount = digicount = 0
    for a in line:
        lowercount += a.islower()
        uppercount += a.isupper()
        digicount += a.isdigit()
    # print("Number of uppercase letters:", uppercount)
    # print("Number of lowercase letters:", lowercount)
    # print("Number of alphabets:", uppercount + lowercount)
    # print("Number of digits:", digicount)
    return ("Number of uppercase letters: {}\nNumber of lowercase letters: {}\n"
        + "Number of digits: {}\nNumber of alphabets: {}").format(uppercount, lowercount, digicount, uppercount + lowercount)


def v2(line: str):
    """Uses filter, and then calulates len. Values are
    stored in a dict with keys = ... in 'Number of ...',
    then values are printed (could be printed, at least) in a loop.
    """

    results = {
        "uppercase letters": len(tuple(filter(lambda x: x.isupper(), line))),
        "lowercase letters": len(tuple(filter(lambda x: x.islower(), line))),
        "digits": len(list(filter(lambda x: x.isdigit(), line))),
    }
    results["alphabets"] = results["uppercase letters"] + results["lowercase letters"]
    return "\n".join(f"Number of {key}: {results[key]}" for key in results)


def v2_2(line: str):
    """Uses filter, and then calulates len. Values are
    stored in a dict with keys = ... in 'Number of ...',
    then values are printed in a loop.

    Might be slower than v2 (isalpha check), but is a  O N E - L I N E R, even though the
    single line is over a few lines (for readability).
    """

    return "\n".join(f"Number of {key}: {value}" 
        for key, value in {
            "uppercase letters": len(tuple(filter(lambda x: x.isupper(), line))),
            "lowercase letters": len(tuple(filter(lambda x: x.islower(), line))),
            "digits": len(list(filter(lambda x: x.isdigit(), line))),
            "alphabets": len(list(filter(lambda x: x.isalpha(), line))),
        }.items())


line = input("Enter a line: ")
print(v2_2(line))
