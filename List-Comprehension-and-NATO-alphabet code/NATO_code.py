import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
code = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in code.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
formatted_code = [code_dict[nato] for nato in word]
print(formatted_code)
