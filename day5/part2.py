with open('input.txt') as home0:
    home=home0.read().split("\n")

good = 0

for i in home:

    good1 = 0
    good2 = 0

    for x, y in zip(i[0:], i[1:]):
        if i.count(x+y) >= 2:
            good1 += 1
    for x,y in zip(i[0:], i[2:]):
        if x == y:
            good2 +=1
    if good1 >= 1 and good2 >=1:
        good +=1



output = open('output2.txt', 'w')
output.write(str(good))

output.close()
home0.close()