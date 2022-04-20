import json

with open('input.txt') as home0:
    home = home0.read()

odb = json.loads(home)

def press_sum(odb):

    i = 0

    if isinstance(odb, str):
        pass
    elif isinstance(odb, int):
        i += odb
    elif isinstance(odb, list):
        for l in odb:
            i += press_sum(l)
    elif isinstance(odb, dict):
        for l in odb:
            i += press_sum(odb[l])

    return i

output = open('output1.txt', 'w')
output.write(str(press_sum(odb)))

output.close()
home0.close()