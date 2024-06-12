#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
# Extract list of names.

name_path = "Input/Names/invited_names.txt"
def extract_names():
    name_file = open(name_path, 'r')
    return [name for name in name_file]
    # print(name_list)

# Extract content of letters
letter_path = "Input/Letters/starting_letter.txt"
def extract_letter_content():
     return open(letter_path, "r").read()
    # print(letter_content)



# Replace [name] with a name from list of names
def replace_name(extracted_names, extracted_letter_content):
    new_letter_path = "Output/ReadyToSend/"
    for name in extracted_names:
        new_letter = extracted_letter_content.replace('[name]',name.replace("\n",""))
        f = open(f'letter_for_{name}.txt',"w")
        f.write(new_letter)
        f.close()
        print(new_letter)



name_list = extract_names()
letter_content = extract_letter_content()
replace_name(name_list, letter_content)