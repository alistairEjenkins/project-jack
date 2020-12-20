import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato = {row.letter:row.code for index, row in data.iterrows()}

print('What is the message? ')
message = input('> ').upper()

coded_message = [nato[letter] for letter in message]

print(coded_message)
