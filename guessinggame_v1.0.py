#last updated 13102021

print("Welcome to my word guessing game! v1.0")

#for game master to enter the secret word
word = input("Key in your secret word here!: ")

guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the word!: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You ran out of guesses!")
else:
    print("You got it!")
