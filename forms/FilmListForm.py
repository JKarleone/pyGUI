from tkinter import *
from forms.FilmForm import FilmForm
from forms.FilmAddingForm import FilmAddingForm
from ClientSocket import Request
from Checker import Checker


class FilmListForm(object):
    def show_btn_clicked(self):
        index = self.box_of_films.curselection()
        if index == "":
            return
        select = self.box_of_films.get(index)
        film = self.films[select]
        self.film_form.show_film_form(film[0], film[1], film[2], film[3],
                                      film[4], film[5], film[6])

    def add_btn_clicked(self):
        self.film_form.hide_form()
        self.change_visibility()
        self.film_adding_form.show_form()

        self.add_btn.place_forget()
        self.back_btn.place(relx=.5, rely=.9, anchor='c')
        self.main.logout_btn.place_forget()
        self.add_film_btn.place(relx=.5, rely=.85, anchor='c')
        self.film_adding_form.error_label.place(relx=.5, rely=.8, anchor='c')

    def back_btn_clicked(self):
        self.change_visibility()
        self.film_adding_form.hide_form()

        self.add_btn.place(relx=.05, rely=.2)
        self.back_btn.place_forget()
        self.main.logout_btn.place(relx=.5, rely=.9, anchor="c")
        self.add_film_btn.place_forget()

    def add_film_btn_clicked(self):
        title = self.film_adding_form.title.get()
        desc = self.film_adding_form.description.get()
        year = self.film_adding_form.year.get()
        actors = self.film_adding_form.actors.get()
        filmmaker = self.film_adding_form.filmmaker.get()
        check = Checker.check_film(title, desc, year, actors, filmmaker)
        print(title, desc, year, actors, filmmaker)

        if check == '':
            request_body = 'film&add&' + title + '&' + desc + '&' + \
                           year + '&' + self.user_id + '&' + actors + '&' + filmmaker
        print('check: ', check)
        self.film_adding_form.error_label['text'] = check

    def __init__(self, window, main_window):
        self.main = main_window
        self.window = window
        self.visible = False

        self.user_id = ''
        self.name = ''
        self.login = ''
        self.usertype = ''
        self.user_label = Label(window, text='', font=('Times', 14))

        # Films collections
        self.film_names = list()
        self.films = dict()
        self.box_of_films = Listbox(width=40, height=22)
        self.update_films()

        self.film_main_label = Label(window, text="Films list", font=("Times", 20))
        self.films_count = Label(window, text="Films count: " + str(len(self.film_names)),
                                 font=("Times", 16))

        self.show_btn = Button(window, text="Show info", width=10, command=self.show_btn_clicked)
        self.add_btn = Button(window, text="Add film", width=10, command=self.add_btn_clicked)
        self.back_btn = Button(window, text="Back", width=12, command=self.back_btn_clicked)
        self.add_film_btn = Button(window, text="Add", width=10, command=self.add_film_btn_clicked)

        self.film_form = FilmForm(window)
        self.film_adding_form = FilmAddingForm(window)

    def change_visibility(self):
        if self.visible:
            self.film_main_label.place_forget()
            self.box_of_films.place_forget()
            self.show_btn.place_forget()
            self.add_btn.place_forget()
            self.films_count.place_forget()
            self.user_label.place_forget()
        else:
            self.film_main_label.place(relx=.5, rely=0.15, anchor="c")
            self.films_count.place(relx=.18, rely=.2)
            self.add_btn.place(relx=.05, rely=.2)
            self.box_of_films.place(relx=0.2, rely=0.55, anchor="c")
            self.show_btn.place(relx=.41, rely=.3, anchor="c")
            self.user_label.place(relx=.5, rely=.95, anchor='c')

        self.visible = not self.visible

    def auth(self, login, name, usertype_id, user_id):
        self.user_id = user_id
        self.login = login
        self.name = name
        self.usertype = usertype_id
        self.user_label['text'] = name + '(' + login + ')'

    def update_films(self):
        self.films = dict()
        self.box_of_films.delete(0, END)
        films_req = Request.request('film&getall').split('\n')
        for film_str in films_req:
            if film_str == '':
                break
            splitted = film_str.split('&')
            self.film_names.append(splitted[0])
            params = list()
            for param in splitted:
                params.append(param)
            self.films[splitted[0]] = params

        for elem in self.film_names:
            self.box_of_films.insert(END, elem)