import re


def zoo(self):
    received_text = input()
    if len(received_text) % 3 != 0:
        return "No"
    occurance_of_z = len(re.findall('z', received_text))
    occurance_of_o = len(re.findall('o', received_text))
    if 2 * occurance_of_z == occurance_of_o:
        return "Yes"
    else:
        return "No"


print(zoo())
