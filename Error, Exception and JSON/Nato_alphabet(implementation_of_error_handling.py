import pandas


code = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in code.iterrows()}
print(code_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        formatted_code = [code_dict[nato] for nato in word]
        print(formatted_code)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
