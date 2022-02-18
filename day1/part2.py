with open("input.txt") as door:
    raw_door = door.read()

good_door =raw_door
j = 0
p = 0
for i in good_door:
    p +=1
    if i == '(':
            j += 1
    else:
            j += -1
    if j == -1:
        break

k = str(p)

output = open ('output2.txt', 'w')
output.write(k)

output.close()
door.close()





