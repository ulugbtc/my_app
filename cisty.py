import random 



cities = ("maskva","jumble","namangan","navoi","iroq","qarshi","istanbul","lingviya","buxoro","farg'ona","toshkent","termiz","xorazm")

word = random.choice(cities)

correct = word 
jumble ="" 

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
    """
            WELCOME TO GAME CITY
            --------------------
    Unscramble the letters to make a word\n
    """
    )

print("The jumble is: ", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("soryy, that's not it. ")
    guess = input("\nYour guess: ")

if guess == correct:
    print("That's it: You guessed it\n")

print("Thanks for playing")
input("\n\nPress the enter key to exit")
