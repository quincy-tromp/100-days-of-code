import pandas as pd

data = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word: ").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)