with open('input.txt') as home0:
    home = home0.read().split('\n')

def check(inp):
    if inp not in inputs:
        return int(inp)

    if isinstance(inputs[inp], int): return inputs[inp]
    return bit(inp)

def bit(inp):
    parts = inputs[inp].split(' ')
    if len(parts) == 1:

        a = parts[0]
        if a in inputs:
            inputs[inp] = check(a)
            return inputs[inp]
        else:
            return  int(a)

    elif len(parts) == 2:

        name,a = parts[0], parts[1]

        if name =="NOT":
            inputs[inp] = ~check(a)
            return inputs[inp]

    elif len(parts) == 3:

        a,name,b =parts[0],parts[1],parts[2]

        if name == "AND":
            inputs[inp] = check(a) & check(b)
            return inputs[inp]
        elif name =="XOR":
            inputs[inp] = check(a) ^ check(b)
            return inputs[inp]
        elif name == "OR":
            inputs[inp] = check(a) | check(b)
            return inputs[inp]
        elif name == "RSHIFT":
            inputs[inp] = check(a) >> check(b)
            return  inputs[inp]
        elif name == 'LSHIFT':
            inputs[inp] = check(a) << check(b)
            return inputs[inp]

inputs = {}

for k in home:

    dad = k.split(' -> ')
    inp,res = dad[0], dad[1]
    inputs[res]= inp

output = open('output1.txt', 'w')
output.write(str(bit('a')))

output.close()
home0.close()















