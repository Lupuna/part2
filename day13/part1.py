def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

with open('input.txt') as home0:
    home = home0.read().split('\n')

happiness = dict()
loc = set()

for i in home:
    name1,_,opinion,qp,_,_,_,_,_,_,name2 = i.split(' ')
    name2 = name2[0:-1]

    if opinion == 'lose':
        happiness[(name1,name2)] = -int(qp)
    else:
        happiness[(name1, name2)] = int(qp)

    loc.add(name1)

best = 0

for raw in permutations(loc):
    sum_happi = 0

    sum_happi += happiness[(raw[0], raw[-1])]
    sum_happi += happiness[(raw[-1], raw[0])]

    for start, end in zip(raw[:-1], raw[1:]):
        sum_happi += happiness[(start,end)]
        sum_happi += happiness[(end,start)]

    best = max(best, sum_happi)


output = open('output1.txt', 'w')
output.write(str(best))

output.close()
home0.close()