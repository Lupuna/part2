import itertools
with open('input.txt') as home0:
    hom = home0.read().split('\n')

home = list([int(i) for i in hom])

ball = 0
i =0

while True:
    for j in itertools.combinations(home, i):
        if sum(j) == 150:
            ball +=1
    if ball > 0:
        break
    i += 1

output = open('output2.txt', 'w')
output.write(str(ball))

output.close()
home0.close()