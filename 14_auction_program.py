logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
clear= lambda : os.system('cls')
print(logo)
print("Welcome to the secret auction program.")
bidders={}
more_bidder=True
while(more_bidder==True):
    Name=input("What is your name?\n")
    bid=int(input("Enter your amount of bid? \n$"))
    ask=input("Are there any more bidders? Yes or No\n")
    bidders[Name]=bid
    if ask=="Yes":
        clear()
        more_bidder=True
    else:
        more_bidder=False

temp = bidders[Name]

for name in bidders:
    if bidders[name]>temp:
        temp = bidders[name]
    else:
        continue
for x in bidders:
    if bidders[x] == temp:
        break

clear()

print(f"The Winner is {x} with a bid of {temp}")