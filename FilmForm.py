from tkinter import *


class FilmForm(object):
    def __init__(self, window):
        self.window = window
        self.visible = False

        self.title = Label(window, font=("Times", 16))

        self.description_label = Label(window, text="Description",
                                       font=("Times bold", 16))
        desc = "Very very very very very very very very very very very very very very long description"
        self.description = Label(window, text=desc, font=("Times", 14), wraplength=350)
        self.year_label = Label(window, font=("Times bold", 16))
        self.year = 1900
        self.score_label = Label(window, font=("Times bold", 16))
        self.score = 10

        self.objects = [self.title, self.description_label]

    def hide_form(self):
        self.title.place_forget()
        self.year_label.place_forget()
        self.score_label.place_forget()
        self.description_label.place_forget()
        self.description.place_forget()

    def get_info_about_film(self, title):
        # Getting data
        print()

    def show_film_form(self, title):
        self.title['text'] = title
        self.title.place(relx=.5, rely=.25)
        self.year_label['text'] = "Year: " + str(self.year)
        self.year_label.place(relx=.5, rely=.3)
        self.score_label['text'] = "Score: " + str(self.score) + "/10"
        self.score_label.place(relx=.5, rely=.35)
        self.description_label.place(relx=.5, rely=.4)
        self.description.place(relx=.5, rely=.45)

