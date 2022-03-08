with open('input.txt') as box0:
    box1 =box0.read().split("\n")
# 2*(a+b)+(a*b*c)

box = [line.split("x") for line in box1[0::]]
feet = 0
for i in box[0::]:
    for j in i[0:1]:
        for k in i[1:2]:
            for d in i[2::]:
                feet += 2*(int(j)+int(k)+int(d))+(int(j)*int(k)*int(d))-2*(max(int(j),int(k),int(d)))


output = open('output2.txt', 'w')
output.write(str(feet))

output.close()
box0.close()