with open('input.txt') as home0:
    home=home0.read().split("\n")

good = 0

for i in home:

    good1 = 0
    good2 = 0
    bad= 0

    for pattern in ['ab', 'cd', 'pq', 'xy']:
        if pattern in i:
            bad += 1
    for x,y in zip(i[0:], i[1:]):
        if x == y:
            good1 +=1
    for b in list(i):
        if b == "a" or b == 'e' or b == 'i' or b == 'o' or b =='u':
            good2 += 1
    if good1 >= 1 and good2 >=3 and bad == 0:
        good +=1


output = open('output1.txt', 'w')
output.write(str(good))

output.close()
home0.close()













