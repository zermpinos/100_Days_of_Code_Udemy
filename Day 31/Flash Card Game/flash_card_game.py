import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


class FlashcardApp:
    def __init__(self):
        self.to_learn = self.load_data()
        self.current_card = {}
        self.flip_timer = None
        self.window = tk.Tk()
        self.canvas = tk.Canvas()
        self.card_front_img = tk.PhotoImage()
        self.card_back_img = tk.PhotoImage()
        self.card_background = None
        self.card_title = None
        self.card_word = None
        self.cross_image = tk.PhotoImage()
        self.unknown_button = tk.Button()
        self.check_image = tk.PhotoImage()
        self.known_button = tk.Button()
        self.create_gui()

    @staticmethod
    def load_data():
        try:
            data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("data/french_words.csv")
            to_learn = original_data.to_dict(orient="records")
        else:
            to_learn = data.to_dict(orient="records")
        return to_learn

    def create_gui(self):
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.canvas = tk.Canvas(width=800, height=526)
        self.card_front_img = tk.PhotoImage(file="images/card_front.png")
        self.card_back_img = tk.PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.cross_image = tk.PhotoImage(file="images/wrong.png")
        self.unknown_button = tk.Button(image=self.cross_image, highlightthickness=0, command=self.next_card)
        self.unknown_button.grid(row=1, column=0)

        self.check_image = tk.PhotoImage(file="images/right.png")
        self.known_button = tk.Button(image=self.check_image, highlightthickness=0, command=self.is_known)
        self.known_button.grid(row=1, column=1)

        self.next_card()

    def next_card(self):
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.to_learn)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)

    def is_known(self):
        self.to_learn.remove(self.current_card)
        data = pandas.DataFrame(self.to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()

    def run(self):
        self.window.mainloop()


app = FlashcardApp()
app.run()
