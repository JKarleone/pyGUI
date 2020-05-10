from tkinter import *
from FilmForm import FilmForm


class FilmListForm(object):
    def show_btn_clicked(self):
        index = self.box_of_films.curselection()
        if index == "":
            return
        select = self.box_of_films.get(index)
        self.film_form.show_film_form(select)

    def add_btn_clicked(self):
        self.film_form.hide_form()
        self.change_visibility()

    def __init__(self, window):
        self.window = window
        self.visible = False

        self.list = list()
        for i in range(0, 50):
            self.list.append("FILE_NAME %i" % i)

        self.film_main_label = Label(window, text="Films list", font=("Times", 20))
        self.films_count = Label(window, text="Films count: " + str(len(self.list)),
                                 font=("Times", 16))

        self.box_of_films = Listbox(width=40, height=22)
        for elem in self.list:
            self.box_of_films.insert(END, elem)
        # self.scroll = Scrollbar(command=self.box_of_films.yview)
        self.show_btn = Button(window, text="Show info", width=10, command=self.show_btn_clicked)
        self.add_btn = Button(window, text="Add film", width=10, command=self.add_btn_clicked)
        self.film_form = FilmForm(window)


    def change_visibility(self):
        if self.visible:
            self.film_main_label.place_forget()
            self.box_of_films.place_forget()
            self.show_btn.place_forget()
            self.films_count.place_forget()
        else:
            self.film_main_label.place(relx=.5, rely=0.15, anchor="c")
            self.films_count.place(relx=.18, rely=.2)
            self.add_btn.place(relx=.05, rely=.2)
            self.box_of_films.place(relx=0.2, rely=0.55, anchor="c")
            self.show_btn.place(relx=.41, rely=.3, anchor="c")

        self.visible = not self.visible
