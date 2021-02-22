import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data = pandas.DataFrame(data)

converted = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(converted)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter Word: ")

for letter in user_input:
    new_list = [converted[word] for word in converted if letter.upper() in word]
    print(new_list)