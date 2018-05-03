import random
randomint = random.randint(1,100)

number=input("Guess a random number between 1-100\n>>")

while int(number) < randomint:
    number = input("Guess higher\n>>")
while int(number) > randomint:
    number = input("guess lower\n>>")
print ("Hurray")

# print("the random number is %s" %(i))
