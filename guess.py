# guess.py (v1)
# 1) Greet the player
print("Welcome to the guessing game!")

# 2) Ask for input. input("...") shows a prompt and returns a text (type: str)
user_text = input("Enter any text and press Enter: ")

# 3) Show what we received
#    Variables (like user_text) are names bound to values.
#    print(...) can print both fixed strings and variables.
print("You typed:", user_text)

# 4) type(...) shows the data type so you can *see* it's a string
print("Data type:", type(user_text))

