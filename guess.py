# guess.py (v2)
print("Welcome to the guessing game!")

# A variable named 'secret' holds our answer (data type: int = integer)
secret = 7

# Ask user for a guess. This returns a *text*.
user_text = input("Enter your guess (whole number): ")

# Convert text like "42" to the integer 42 using int(...).
# NOTE: If user_text isn't numeric, int(...) will raise a ValueError. We'll handle that next.
guess = int(user_text)

# if/elif/else chooses exactly one branch based on conditions.
# '==' checks equality; '<' and '>' compare numbers.
if guess == secret:
    print("Congratulations! You guessed it right.")
elif guess < secret:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")
