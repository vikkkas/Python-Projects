# Split string method
names_string = input("Give me everybody's names, separated by a comma\', \'. ")
names = names_string.split(", ")

l=len((names))

import random
random_name=random.randint(0,l-1)
name=names[random_name]
print(f"{name} is going to pay the bill today!")