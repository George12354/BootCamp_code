# TODO: Create a letter using starting_letter.docx
#  for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyTOSend".
#  Hint1: This method will help you:
#  https:/www.w3schools.com/python/ref_file_readlines.asp
#      Hint2: This method will also help you:
#      https://www.w3schools.com/python/ref_string_replace.asp
#          Hint3: This method will help you:
#          https://www.w3schools.com/python/ref_string_strip.asp


f = open("Input/Names/invited_names.txt", "r")
new_f = f.readlines()
# print(new_f)

with open("Input/Letters/starting_letter.docx", "r") as file:
    contents = file.read()
    # print(contents)


for names in new_f:
    x = names.strip("\n")
    new_g = contents.replace("[name]", f"{x}")
    # print(new_g)
    with open(f"Output/ReadyToSend/{x}.docx", "w") as fill:
        fill.write(new_g)

