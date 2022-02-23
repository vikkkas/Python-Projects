print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
convert1=name1.lower()
convert2=name2.lower()
name=convert1+convert2
add1=name.count("t")
add2=name.count("r")
add3=name.count("u")
add4=name.count("e")
score1=str(int(add1+add2+add3+add4))
add5=name.count("l")
add6=name.count("o")
add7=name.count("v")
add8=name.count("e")
score2=str(int(add5+add6+add7+add8))
finalscore=int(score1+score2)

if finalscore<=10or finalscore>=90:
  print(f"Your score is {finalscore},you go together like coke and mentos.")
elif finalscore>=40and finalscore<=50:
  print(f"Your score is {finalscore}, you are alright together.")
else:
  print(f"Your score is {finalscore}.")
