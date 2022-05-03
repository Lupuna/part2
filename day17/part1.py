import itertools
with open('input.txt') as home0:
    hom = home0.read().split('\n')

home = list([int(i) for i in hom])

ball = 0

for i in range(len(home)):
    for j in itertools.combinations(home, i):
        if sum(j) == 150:
            ball +=1

output = open('output1.txt', 'w')
output.write(str(ball))

output.close()
home0.close()

