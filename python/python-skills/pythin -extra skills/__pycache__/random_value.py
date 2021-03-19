import random


for i in range(3):      # generating 3 random values at a time
    print(random.random())

for i in range(3):      # generating 3 random values between 1 to 5
    print(random.randint(1,5))

x=random.random()       # generating single random value
print(x)

members=["ali","faiz","salman"]
leader = random.choice(members)   # choosing a random leader from members
print(leader)   

class dice:
    # def roll(self):                       #first method
    #     elements=[1,2,3,4,5,6]
    #     x=random.choice(elements)
    #     y=random.choice(elements)
    #     t=(x,y)
    #     return(t)

    def roll(self):
        elements=[1,2,3,4,5,6]
        x=random.randint(1,6)
        y=random.randint(1,6)
        t=(x,y)
        return(t)

print(dice().roll())
#print(a)