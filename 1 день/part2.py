with open("input.txt") as door:
    raw_door = door.read()

good_door =(list(raw_door))
j = 0
for i in good_door:
    if i == ')':
        j += -1
    elif i == '(':
        j += 1

i = str(j)

output = open ('output2.txt', 'w')
output.write(i)

output.close()
door.close()