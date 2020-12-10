
class Quizmaster:

    def __init__(self, name = input('What is the name of the Quizmaster? ')):
        self.name = name

    def intro(self, title):
        print(f'Welcome to the {title}!')
        print(f"I'm your host {self.name} ... ")
        print(" ... Let's meet out lovely contestant.")

    def greet(self, c):
        print("Hello and what's your name? ")
        c.name = (input('> '))
        print(f'Hello {c.name}. Welcome to the show!')

    def ask(self,q,c):

        for num in range(0, len(q.qs) - 1):
            print(f'Okay {c.name} here is question number {num + 1}')
            print(f"Q: {q.qs[num]['text']}? True or False?)")
            ans = input('True/False? ')
            if ans == q.qs[num]['answer']:
                print('Congratulations, that is correct!')
                c.score += 1
            else:
                print("I'm sorry, that is not correct")
            print(f"Your current score is {c.score}/{num + 1}")


    def total_score(self,c):
        print(f'total score : {c.score}')

