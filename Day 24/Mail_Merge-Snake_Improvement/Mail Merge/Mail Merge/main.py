import os

PLACEHOLDER = "[name]"

# Read names from the file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

# Read the letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Create the output directory if it doesn't exist
os.makedirs("./Output/ReadyToSend", exist_ok=True)

# Generate personalized letters
for name in names:
    new_letter = letter_contents.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
