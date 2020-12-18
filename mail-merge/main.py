names = []

with open('mail-merge-project-start/Input/Names/invited_names.txt') as invited:
    name_s = invited.readlines()
    for name in name_s:
        name = name.strip('\n')
        names.append(name)

with open('mail-merge-project-start/Input/Letters/starting_letter.docx') as letter_template:
    letter = letter_template.read()

    for name in names:
        letter = letter.replace('[name]', name)
        with open(f'mail-merge-project-start/Output/ReadyToSend/{name}.docx', 'w+') as named_letter:
            named_letter.write(letter)



