from random import randint
print("Hello! What is your name?")
name = input()
print()
print("Well, " + name + ", I am thinking of a number between 1 and 20." )
n = randint(1, 20)
c = 0
i = 1
print("Take a guess.")
while True:
    c = int(input())
    if c < n:
        print("Your guess is too low.")
        print("Take a guess.")
    elif c > n:
        print("Your guess is too high.")
        print("Take a guess.")
    else:
        print("Good job, " + name +"! You guessed my number in", i, "guesses!")
        break
    i += 1
