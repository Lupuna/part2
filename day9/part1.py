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


dist = dict()
loc = set()
for i in home:
    start,_,end,_,qp = i.split(' ')
    dist[(start,end)] = int(qp)
    dist[(end,start)] = int(qp)
    loc.add(start)
    loc.add(end)

best = 1000000000000000000

for raw in permutations(loc):
    km = 0
    for start, end in zip(raw, raw[1:]):

        km += dist[(start,end)]

    if km < best:
        best = km

output = open('output1.txt', 'w')
output.write(str(best))

output.close()
home0.close()










# dist= dict()
# loc1 = list()
# loc2 = list()
#
# for i in home:
#     start,to,end,qp,km = i.split(' ')
#     dist[(start,end)] = int(km)
#     if loc1.count(start) >= 1:
#         pass
#     else:
#         loc1.append(start)
#     if loc2.count(start) >= 1:
#         pass
#     else:
#         loc2.append(end)
#
#
# i = []
# for a in loc1:
#     l = []
#     for b in loc2:
#         km = 0
#         try:
#             l.append(dist[(a,b)])
#         except:
#             continue
#
#     for d in loc2:
#         km = 0
#         try:
#             if dist[(a,d)] == min(l):
#                 print(d)
#         except:
#             continue

