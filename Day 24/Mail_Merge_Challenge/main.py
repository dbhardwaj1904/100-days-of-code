PLACEHOLDER = "[user_name]"

with open("./Names/invite_names.txt") as names:
    user_names = names.readlines()

with open("./Input/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in user_names:
        stripped_name = name.strip()
        letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/letter_for_{stripped_name}.txt", mode="w") as invite_letter:
            invite_letter.write(letter)
