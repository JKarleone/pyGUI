from tkinter import *


class FilmForm(object):
    def __init__(self, window):
        self.window = window
        self.visible = False

        self.title = Label(window, font=("Times", 18))

        self.description_label = Label(window, text='Description:',
                                       font=('Times', 16))
        self.description_text = Label(window, font=('Times', 12), wraplength=350)
        self.year_label = Label(window, font=('Times', 16))

        self.actors_label = Label(window, font=('Times', 14), wraplength=300)

        self.filmmaker_label = Label(window, font=('Times', 16))

        self.creator_label = Label(window, font=('Times', 14))

        self.score_label = Label(window, font=('Times', 14))

    def hide_form(self):
        self.title.place_forget()
        self.year_label.place_forget()
        self.score_label.place_forget()
        self.description_label.place_forget()
        self.description_text.place_forget()
        self.actors_label.place_forget()
        self.filmmaker_label.place_forget()
        self.creator_label.place_forget()

    def show_film_form(self, title, desc, year, score,
                       creator, actors, filmmaker):
        self.title['text'] = title
        self.title.place(relx=.5, rely=.25)

        self.year_label['text'] = 'Year: ' + str(year)
        self.year_label.place(relx=.5, rely=.3)

        self.filmmaker_label['text'] = 'Filmmaker: ' + filmmaker
        self.filmmaker_label.place(relx=.5, rely=.35)

        self.score_label['text'] = 'Score: ' + str(score) + "/5"
        self.score_label.place(relx=.5, rely=.4)

        self.creator_label['text'] = 'Creator: ' + creator
        self.creator_label.place(relx=.5, rely=.45)

        self.actors_label['text'] = 'In leading roles: ' + actors
        self.actors_label.place(relx=.5, rely=.5)

        self.description_label.place(relx=.5, rely=.58)
        self.description_text['text'] = desc
        self.description_text.place(relx=.5, rely=.63)
