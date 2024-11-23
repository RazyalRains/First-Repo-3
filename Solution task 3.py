import random
words = ["Watermelons", "Apples", "Bananas", "Redirect"]
choosen = random.choice(words)
l = list(choosen)
random.shuffle(l)
scrambled = "".join(l)
tries = 5
count = 0
print("Welcome to the word guessing game!")
print("You have 5 tries to try and guess the following scrambled word: ",scrambled)
while tries>count:
    x = input("Please enter your guess: ")
    if x == choosen:
        print("Congrats, you got it right!")
        break
    elif x != choosen and x !="":
        remaining = tries-count-1
        print("You got it wrong, please try again, you have ",remaining," tries left!")
        count +=1
        if not x: print("Please enter your guess: ")
        if count == tries:
            print("You have used up all of your tries! :( ")
            print("The correct word was "+choosen+"!")
#Explanation is in the readme file in the second link!
