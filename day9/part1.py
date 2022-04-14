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

best = 1000000000000000000

for raw in itertools.permutations(loc):
    print(raw)
    km = 0
    for start, end in zip(raw, raw[1:]):

        km += dist[(start,end)]

    if km < best:
        best = km
print(best)
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

