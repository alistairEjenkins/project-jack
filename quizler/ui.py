from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f'Score: 0', bg=THEME_COLOR, fg='white', font=('Courier',20,'bold'))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, text='question?', width=280,font=('Arial',20,'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady= 50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have completed the quiz.')
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')
                                                            
    def true_pressed(self):
        answer = 'true'
        self.confirm_answer(self.quiz.check_answer(answer))

    def false_pressed(self):
        answer = 'false'
        self.confirm_answer(self.quiz.check_answer(answer))

    def confirm_answer(self,correct):

        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score.config(text= f'Score: {self.quiz.score}')
        self.window.after(1000, self.get_next_question)
