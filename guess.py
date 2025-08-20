# guess.py (v2)
print("Welcome to the guessing game!")

# A variable named 'secret' holds our answer (data type: int = integer)
secret = 7

# Ask user for a guess. This returns a *text*.
user_text = input("Enter your guess (whole number): ")

try:
    guess = int(user_text)  # Convert text to an integer
except ValueError:
    print("Invalid input! Please enter a whole number.")
else:
    if guess == secret:
        print("Congratulations! You guessed it right.")
    elif guess < secret:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")