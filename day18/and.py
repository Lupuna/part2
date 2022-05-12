import random
with open('input.txt') as home0:
    home = home0.read().split('\n')

def randomaiser(ing : list):

    step1 = random.randint(0,100)
    step2 = random.randint(0,100)
    step3 = random.randint(0,100)
    step4 = random.randint(0,100)

    suma  = ing[0] * step1 + ing[1] * step2 + ing[2] * step3 + ing[3] * step4
    if suma <= 0 or step1+step2+step3+step4 > 100:
        return randomaiser(ing)
    return suma

ingredients = dict()

for i in home:
    name,_,capacity,_,durability,_,flavor,_,texture,_,calories= i.split(' ')
    capacity, durability, flavor, texture = capacity[0:-1], durability[0:-1], flavor[0:-1], texture[0:-1]
    ingredients[name] =[int(capacity),int(durability),int(flavor),int(texture)]

ingredient1 = []
ingredient2 = []
ingredient3 = []
ingredient4 = []

[ingredient1.append(j[0]) for i,j in ingredients.items()]
[ingredient2.append(j[1]) for i,j in ingredients.items()]
[ingredient3.append(j[2]) for i,j in ingredients.items()]
[ingredient4.append(j[3]) for i,j in ingredients.items()]

i = 0
proportions = []
while i <= 50000:
    proportions.append(randomaiser(ingredient1)*randomaiser(ingredient2)*randomaiser(ingredient3)*randomaiser(ingredient4))
    i += 1
print(max(proportions))