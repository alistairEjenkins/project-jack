from quiz import Quiz
from quizmaster import Quizmaster
from contestant import Contestant

def main():

    q = Quiz()
    qm = Quizmaster()
    c = Contestant()
    qm.intro(q.title)
    qm.greet(c)
    qm.ask(q,c)
    qm.total_score(c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
