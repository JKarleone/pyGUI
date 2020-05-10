from tkinter import *
from LoginForm import LoginForm
from RegisterForm import RegisterForm
from FilmListForm import FilmListForm


class MainWindow(object):
    # Buttons clicked action
    def logout_btn_clicked(self):
        self.change_login_form_visibility()
        self.change_film_list_form_visibility()

    def login_btn_clicked(self):
        self.change_login_form_visibility()
        self.change_film_list_form_visibility()

    def register_btn_clicked(self):
        self.change_register_form_visibility()
        self.change_film_list_form_visibility()

    # Buttons visibility
    def change_footer_btn_visibility(self):
        if self.film_list_form.visible:
            self.footer_btn.place_forget()
        else:
            self.footer_btn.place(relx=.5, rely=.9, anchor="c")

    def change_logout_btn_visibility(self):
        if self.film_list_form.visible:
            self.logout_btn.place_forget()
        else:
            self.logout_btn.place(relx=.5, rely=.9, anchor="c")

    def change_login_btn_visibility(self):
        if self.login_form.visible:
            self.login_button.place_forget()
        else:
            self.login_button.place(relx=.5, rely=0.57, anchor="c")

    def change_register_btn_visibility(self):
        if self.register_form.visible:
            self.register_button.place_forget()
        else:
            self.register_button.place(relx=.5, rely=0.72, anchor="c")

    # Forms Visibility
    def change_login_form_visibility(self):
        self.change_login_btn_visibility()
        self.login_form.change_visibility()

    def change_register_form_visibility(self):
        self.change_register_btn_visibility()
        self.register_form.change_visibility()

    def change_film_list_form_visibility(self):
        self.change_logout_btn_visibility()
        self.film_list_form.change_visibility()
        self.change_footer_btn_visibility()
        self.film_list_form.film_form.hide_form()

    # Swipe Login and Register Form on button click
    def change_form(self):
        if self.login_form.visible:
            self.footer_btn['text'] = "Login"
        else:
            self.footer_btn['text'] = "Registration"
        self.change_login_form_visibility()
        self.change_register_form_visibility()

    def __init__(self):
        self.window = Tk()
        self.window.title('Film Library')
        self.window.geometry('800x600')

        main_label = Label(self.window, text="Film Library", font=("Times", 30))
        main_label.pack(side=TOP, fill=Y)

        # Login Form
        self.login_form = LoginForm(self.window)
        self.login_button = Button(self.window, text="SIGN IN", width=16,
                                   bg='#FF5722', fg='white',
                                   command=self.login_btn_clicked)
        self.login_button.place(relx=.5, rely=0.57, anchor="c")

        # Registering Form
        self.register_form = RegisterForm(self.window)
        self.register_button = Button(self.window, text="SIGN UP", width=16, bg='#FF5722', fg='white',
                                      command=self.register_btn_clicked)

        # List of all films Form
        self.film_list_form = FilmListForm(self.window)

        self.logout_btn = Button(self.window, text="Log out", width=12, command=self.logout_btn_clicked)

        self.footer_btn = Button(self.window, text="Registration", width=12, command=self.change_form)
        self.footer_btn.place(relx=.5, rely=.9, anchor="c")
