from tkinter import *
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm
from forms.FilmListForm import FilmListForm
from client.Client import Request
from client.Checker import Checker


class MainWindow(object):
    # Buttons clicked action
    def logout_btn_clicked(self):
        self.change_login_form_visibility()
        self.change_film_list_form_visibility()
        self.footer_btn['text'] = "Registration"

    def login_btn_clicked(self):
        login = self.login_form.login.get()
        password = self.login_form.password.get()
        check = Checker.check_auth(login, password)
        if check == '':
            request_body = 'auth&' + login + '&' + password
            ans = Request.request(request_body)
            print(ans)
            if ans != 'auth error' and ans != 'can\'t connect to server':
                user_params = ans.split('&')
                self.film_list_form.auth(login, user_params[1], user_params[0], user_params[2])
                self.change_login_form_visibility()
                self.change_film_list_form_visibility()
                self.error_label['text'] = ''
            else:
                check = ans

        self.error_label['text'] = check
        self.login_form.clear_entries()

    def register_btn_clicked(self):
        login = self.register_form.login.get()
        name = self.register_form.name.get()
        password = self.register_form.password.get()
        check = Checker.check_reg(login, name, password)
        if check == '':
            request_body = 'reg&' + login + '&' + password + '&' + name
            ans = Request.request(request_body)
            if ans.isdigit():
                self.film_list_form.auth(login, name, 1, ans)
                self.change_register_form_visibility()
                self.change_film_list_form_visibility()
                self.error_label['text'] = ''
            else:
                check = ans

        self.error_label['text'] = check
        self.register_form.clear_entries()

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
            self.register_button.place(relx=.5, rely=0.62, anchor="c")

    # Forms Visibility
    def change_login_form_visibility(self):
        self.change_login_btn_visibility()
        self.login_form.change_visibility()
        self.error_label['text'] = ''

    def change_register_form_visibility(self):
        self.change_register_btn_visibility()
        self.register_form.change_visibility()
        self.error_label['text'] = ''

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
        self.window.resizable(width=False, height=False)

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

        # Error label
        self.error_label = Label(self.window, text='', font=('Times', 14), fg='#FF0000')
        self.error_label.place(relx=.5, rely=0.7, anchor="c")

        # List of all films Form
        self.film_list_form = FilmListForm(self.window, self)

        # Log out btn
        self.logout_btn = Button(self.window, text="Log out", width=12, command=self.logout_btn_clicked)

        # Registration/Login btn
        self.footer_btn = Button(self.window, text="Registration", width=12, command=self.change_form)
        self.footer_btn.place(relx=.5, rely=.9, anchor="c")
