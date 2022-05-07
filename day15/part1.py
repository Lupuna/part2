import functools

with open('input.txt') as home0:
    home = home0.read()

idict = dict()

def prod(lst):
    return functools.reduce(lambda x,y: x*y,lst)

def optimize (ings, remaining, sofar):
    if len(ings) == 0 or remaining == 0:
        return prod([max(0,x) for x in sofar])

    name, features = ings[0]
    if len(ings) == 1:
        return  prod([max(0,remaining*a+b) for a,b in zip(features,sofar)])

    best = -10000000000000000000
    for i in range(0,remaining+1):
        newsofar = [i*a+b for a,b in zip(features,sofar)]
        score = optimize(ings[1:], remaining-i, newsofar)
        if score > best: best = score
    return best

for line in home.split('\n'):
    n,fstr = line.split(': ')
    features = []
    for feat in fstr.split(', '):
        fname,fval = feat.split(' ')
        features.append(int(fval))
    idict[n] = features[:-1]

zing = [(iname, features) for iname, features in idict.items()]

otvet = optimize(zing, 100, [0]*4)

output = open('output1.txt', 'w')
output.write(str(otvet))

output.close()
home0.close()
