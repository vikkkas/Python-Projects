#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill=input("what was the total bill?")
#alt we can use
#bill=float(input("what was the total bill?"))
tip=input("How much tip would you like to give?")
n=input("How many people to split the bill?")
bill=float(bill)
tip=int(tip)
n=int(n)
total= (bill + (tip*.01*bill))/n
print(round(total,2))
#alternate for round off
#total  {:.2f}.format(total)  
