from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#2f3640"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizly")
        self.root.config(padx=40, pady=40, background=THEME_COLOR)
        self.root.eval('tk::PlaceWindow . center')

        # Setting up the score label
        self.score = 0
        self.score_text = Label(
            text=f"Score: {self.score}", background=THEME_COLOR, highlightthickness=0, fg="white", font=("Arial", 16))
        self.score_text.grid(column=0, row=0)

        # Setting up the canvas
        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Question", font=("Arial", 16, "italic"), fill="black")

        # Setting up the button images
        self.true_img = PhotoImage(file="gui based quiz app/images/true.png")
        self.false_img = PhotoImage(file="gui based quiz app/images/false.png")

        # Setting up the btns
        self.btn_true = Button(width=100, height=100, bg=THEME_COLOR, bd=0, activebackground=THEME_COLOR,
                               image=self.true_img, highlightthickness=0, command=self.select_true)
        self.btn_true.grid(column=0, row=2)
        self.btn_false = Button(width=100, height=100, bg=THEME_COLOR, bd=0, activebackground=THEME_COLOR,
                                image=self.false_img, highlightthickness=0, command=self.select_false)
        self.btn_false.grid(column=1, row=2)

        self.next_question()

        self.root.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions() == True:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.btn_true.config(state="normal")
            self.btn_false.config(state="normal")
        else:
            self.canvas.itemconfig(
                self.question_text, text=f"Game over!\nScore: {self.score}")

    def select_true(self):
        self.btn_true.config(state="disabled")
        self.btn_false.config(state="disabled")
        if self.quiz.check_answer(user_answer="true") == True:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def select_false(self):
        self.btn_true.config(state="disabled")
        self.btn_false.config(state="disabled")
        if self.quiz.check_answer(user_answer="true") == False:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, correct):
        if correct == True:
            self.canvas.config(background="green")
            self.root.after(1000, self.next_question)
        else:
            self.canvas.config(background="red")
            self.root.after(1000, self.next_question)
