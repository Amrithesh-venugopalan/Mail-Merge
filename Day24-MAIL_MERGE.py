SAMPLE_NAME="[name]"

with open("../Desktop/python codes/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    name_list=names_file.readlines()
    print(name_list)
with open("../Desktop/python codes/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_content=letter_file.read()
    for name in name_list:
        stripped_name=name.strip()
        new_letter=letter_content.replace(SAMPLE_NAME, stripped_name)
        with open(f"../Desktop/python codes/Mail Merge Project Start/Output/ReadyToSend/Letter_for_{stripped_name}.txt","w") as final_letter:
            final_letter.write(new_letter)
