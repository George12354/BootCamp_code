from tkinter import *
from quiz_brain import QuizBrain

# importing the quiz_brain was to help set the particular data type

THEME_COLOR = "#375362"
red = "#FF0000"
white = "#FFFFFF"
green = "#00FF00"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.is_right = None
        self.window = Tk()
        self.quiz = quiz_brain
        # The variable Quizbrain was used as a means to pass a datatype to the parameter
        # quiz_brain: QuizBrain
        # Used the format above to assign the datatype QuizBrain to...
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text=" ", font=("Ariel", 15, "bold"),
                           bg=THEME_COLOR, fg="white", pady=20)

        self.score.grid(column=1, row=0, columnspan=2)
        # the width in question text was to make the question fit within the canvas.
        self.question_text = self.canvas.create_text(150, 107, text='some question text', width=280,
                                                     font=("Arial", 15, "italic"))

        self.right_image = PhotoImage(file="images/true.png")
        self.r_button = Button(image=self.right_image, highlightthickness=0, command=self.r_ans)
        self.r_button.grid(column=0, row=3)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.w_button = Button(image=self.wrong_image, highlightthickness=0, command=self.w_ans)
        self.w_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.r_button.config(state="disabled")
            self.w_button.config(state="disabled")

    def r_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def w_ans(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.is_right = is_right

        if self.is_right == "True":
            self.canvas.config(bg=green)

        else:
            self.canvas.config(bg=red)

        self.window.after(0, self.give_feedback)
        self.window.after(1000, self.reset_color)
        # print(f"Button clicked : {self.is_right}")
        # print(f"Did the button you clicked match? : {self.quiz.correct_answer}")
        # print(len(self.quiz.question_list))

    def reset_color(self):
        self.canvas.config(bg=white)
        self.get_next_question()
