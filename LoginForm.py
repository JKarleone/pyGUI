from tkinter import *


class LoginForm(object):
    def __init__(self, window):
        self.window = window
        self.visible = False

        self.sign_in_label = Label(window, text="SIGN IN", font=("Times", 24))

        self.login_label = Label(window, text="Login", font=("Times", 16))
        self.login_entry = Entry(window, width=22)

        self.password_label = Label(window, text="Password", font=("Times", 16))
        self.password_entry = Entry(window, width=22, show='*')

        self.change_visibility()

    def change_visibility(self):
        if self.visible:
            self.sign_in_label.place_forget()

            self.login_label.place_forget()
            self.login_entry.place_forget()

            self.password_label.place_forget()
            self.password_entry.place_forget()
        else:
            self.sign_in_label.place(relx=.5, rely=.25, anchor="c", bordermode=OUTSIDE)

            self.login_label.place(relx=.5, rely=0.35, anchor="c")
            self.login_entry.place(relx=.5, rely=0.4, anchor="c")

            self.password_label.place(relx=.5, rely=0.45, anchor="c")
            self.password_entry.place(relx=.5, rely=0.5, anchor="c")

        self.visible = not self.visible
