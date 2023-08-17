import random 

print(input("Press any key to toss the coin ")) 

random_int = random.randint(0, 1) 

if random_int == 0:
    print("Heads")
else:
    print("Tails") 
