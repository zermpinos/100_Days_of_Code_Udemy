import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = dict(zip(data["letter"], data["code"]))
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
