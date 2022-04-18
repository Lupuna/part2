with open('input.txt') as home0:
    home = home0.read()

al='abcdfghijkmnpqrstuvwxyz'
stop = ['i', 'l', 'o']
alal ='''abc
bcd
cdi
dif
ifg
fgh
ghi
hij
ijk
jkl
klm
lmn
mno
nop
opq
pqr
qrs
rst
stu
tuv
uvw
vwx
wxy
xyz'''
alal = alal.split('\n')
next_letter = {c1: c2 for c1, c2 in zip(al, al[1:]+'a')}
doubles = [c+c for c in al]

def next_password(s):
    s = s[:-1] + next_letter[s[-1]]
    for i in range(-1, -8, -1):
        if s[i] == 'a':
            s = s[:i-1] + next_letter[s[i-1]] + s[i:]
        else:
            break
    return s

def stop_mod(s):

    count = 0

    if sum([i in s for i in doubles]) >= 2:
        for g, p, k in zip(s, s[1:], s[2:]):
            if alal.count(g + p + k) >= 1:
                count += 1

    if count > 0:
        return True
    else:
        return False



while stop_mod(home) == False:
    home = next_password(home)

output = open('output1.txt', 'w')
output.write(str(home))

output.close()
home0.close()




















