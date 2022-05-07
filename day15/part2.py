import functools

with open('input.txt') as home0:
    home = home0.read()

idict = dict()

def prod(lst):
    return functools.reduce(lambda x,y: x*y,lst)

def optimize (ings, remaining, sofar, calories):
    if len(ings) == 0 or remaining == 0:
        if calories != 500: return -10000000000000000000
        return prod([max(0,x) for x in sofar])

    name, features = ings[0]
    if len(ings) == 1:
        if remaining*features[-1]+calories != 500: return -10000000000000000000
        return  prod([max(0,remaining*a+b) for a,b in zip(features,sofar)])

    best = -10000000000000000000
    for i in range(0,remaining+1):
        newsofar = [i*a+b for a,b in zip(features[:-1],sofar)]
        score = optimize(ings[1:], remaining-i, newsofar, calories+i*features[-1])
        if score > best: best = score
    return best

for line in home.split('\n'):
    n,fstr = line.split(': ')
    features = []
    for feat in fstr.split(', '):
        fname,fval = feat.split(' ')
        features.append(int(fval))
    idict[n] = features

zing = [(iname, features) for iname, features in idict.items()]

otvet = optimize(zing, 100, [0]*4,0)

output = open('output2.txt', 'w')
output.write(str(otvet))

output.close()
home0.close()