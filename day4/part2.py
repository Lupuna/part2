import hashlib
with open('input.txt') as home0:
    home = home0.read()
print(home)
i = 1
while True:

    md5 = hashlib.md5((home+str(i)).encode())

    if md5.hexdigest().startswith('000000'):
        break

    i += 1

output = open('output2.txt', 'w')
output.write(str(i))

output.close()
home0.close()