import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
word=random.choice(word_list)

list=[]
for x in range(len(word)):
    list.append("_")

end_of_game = False

lives = 6

while not end_of_game:
    guess = input("Enter a letter:")
    guess=guess.lower()

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
          list[position] = guess

    if guess not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(list)}")

    if "_" not in list: #Include this in notes
        end_of_game = True
        print("You Win!")
    
    print(stages[lives])
