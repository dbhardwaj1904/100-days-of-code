import pandas
from tkinter import *
import random

BG = "#B1DDC6"
current_card = {}
learn_words = {}
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origin_file = pandas.read_csv("data/french_words.csv")
    learn_words = origin_file.to_dict(orient="records")
else:
    learn_words = data_file.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn_words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_foreground, image=card_front)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_foreground, image=card_back)


def guessed__correct():
    learn_words.remove(current_card)
    data = pandas.DataFrame(learn_words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BG)

flip_timer = window.after(5000, func=flip_card)

# Front image
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_foreground = canvas.create_image(400, 263, image=card_front)
card_background = canvas.create_image(400, 263, image=card_back)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(background=BG, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Right Button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=guessed_correct)
right_button.grid(row=1, column=1)

window.mainloop()
