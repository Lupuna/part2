import itertools

with open('input.txt') as home0:
    home = home0.read().split('\n')


dist = dict()
loc = set()
for i in home:
    start,_,end,_,qp = i.split(' ')
    dist[(start,end)] = int(qp)
    dist[(end,start)] = int(qp)
    loc.add(start)
    loc.add(end)

best = 0
for raw in itertools.permutations(loc):
    km = 0
    for start, end in zip(raw, raw[1:]):

        km += dist[(start,end)]

    if km > best:
        best = km
print(best)
output = open('output2.txt', 'w')
output.write(str(best))

output.close()
home0.close()
