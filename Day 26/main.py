import pandas


def generate_words():
    username = input("Enter word to spell?: ").upper()
    try:
        user_list = [user_dic[letter] for letter in username]
    except KeyError:
        print("Sorry, only alphabets or letters allowed.")
        generate_words()
    else:
        print(user_list)


data_file = pandas.read_csv("nato_phonetic_alphabet.csv")
user_dic = {row.letter: row.code for (index, row) in data_file.iterrows()}
generate_words()