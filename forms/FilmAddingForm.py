from tkinter import *


class FilmAddingForm(object):
    def __init__(self, window):
        self.window = window
        self.visible = False

        self.title = StringVar()
        self.description = StringVar()
        self.year = StringVar()
        self.actors = StringVar()
        self.filmmaker = StringVar()

        self.title_label = Label(window, text='Title', font=('Times', 18))
        self.title_entry = Entry(window, width=25, textvariable=self.title)

        self.description_label = Label(window, text='Description', font=('Times', 18))
        self.description_entry = Entry(window, width=50, textvariable=self.description)

        self.year_label = Label(window, text='Year', font=('Times', 18))
        self.year_entry = Entry(window, width=25, textvariable=self.year)

        self.actors_label = Label(window, text='Actors', font=('Times', 18))
        self.actors_entry = Entry(window, width=50, textvariable=self.actors)

        self.filmmaker_label = Label(window, text='Filmmaker', font=('Times', 18))
        self.filmmaker_entry = Entry(window, width=25, textvariable=self.filmmaker)

        self.error_label = Label(window, text='', font=('Times', 16), fg='#FF0000')

    def show_form(self):
        self.title_label.place(relx=.5, rely=.25, anchor='c')
        self.title_entry.place(relx=.5, rely=.3, anchor='c')

        self.description_label.place(relx=.5, rely=.35, anchor='c')
        self.description_entry.place(relx=.5, rely=.4, anchor='c')

        self.year_label.place(relx=.5, rely=.45, anchor='c')
        self.year_entry.place(relx=.5, rely=.5, anchor='c')

        self.actors_label.place(relx=.5, rely=.55, anchor='c')
        self.actors_entry.place(relx=.5, rely=.6, anchor='c')

        self.filmmaker_label.place(relx=.5, rely=.65, anchor='c')
        self.filmmaker_entry.place(relx=.5, rely=.7, anchor='c')

        self.error_label.place(relx=.5, rely=.75, anchor='c')

    def hide_form(self):
        self.title_label.place_forget()
        self.title_entry.place_forget()
        self.title_entry.delete(0, END)

        self.description_label.place_forget()
        self.description_entry.place_forget()
        self.description_entry.delete(0, END)

        self.year_label.place_forget()
        self.year_entry.place_forget()
        self.year_entry.delete(0, END)

        self.actors_label.place_forget()
        self.actors_entry.place_forget()
        self.actors_entry.delete(0, END)

        self.filmmaker_label.place_forget()
        self.filmmaker_entry.place_forget()
        self.filmmaker_entry.delete(0, END)

        self.error_label.place_forget()
        self.error_label['text'] = ''
