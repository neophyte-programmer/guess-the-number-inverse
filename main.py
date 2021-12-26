import random


def computerGuess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            high = guess + 1

    print("Yay! I guessed your number correctly")


print("Choose a number for me to guess and don't tell me.")
y = int(input("Now, give me a reasonable upper range to guess within: "))

computerGuess(y)
