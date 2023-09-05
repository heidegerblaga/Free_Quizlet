from model import Lern, session

verb_list = [
    ('awake', 'awoke', 'awoken'),
    ('be', 'was/were', 'been'),
    # Dodaj pozostałe czasowniki tutaj
]



# Zatwierdź zmiany
session.commit()

with open("czasowniki.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.split('-'))
        verb = Lern(polish=line.split('-')[3].strip(),
        infinitive =line.split('-')[0].strip(), simple_past = line.split('-')[1].strip(), past_participle = line.split('-')[2].strip(),point=0)
#         session.add(verb)
#
# session.commit()

        # Plik jest już zamknięty poza blokiem 'with'
