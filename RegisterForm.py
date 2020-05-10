from tkinter import *


class RegisterForm(object):
    def __init__(self, window):
        self.window = window
        self.visible = False

        self.sign_up_label = Label(window, text="SIGN UP", font=("Times", 24))

        self.login_label = Label(window, text="Login", font=("Times", 16))
        self.login_entry = Entry(window, width=22)

        self.email_label = Label(window, text="Email", font=("Times", 16))
        self.email_entry = Entry(window, width=22)

        self.name_label = Label(window, text="Name", font=("Times", 16))
        self.name_entry = Entry(window, width=22)

        self.password_label = Label(window, text="Password", font=("Times", 16))
        self.password_entry = Entry(window, width=22, show='*')

    def change_visibility(self):
        if self.visible:
            self.sign_up_label.place_forget()

            self.login_label.place_forget()
            self.login_entry.place_forget()

            self.email_label.place_forget()
            self.email_entry.place_forget()

            self.name_label.place_forget()
            self.name_entry.place_forget()

            self.password_label.place_forget()
            self.password_entry.place_forget()
        else:
            self.sign_up_label.place(relx=.5, rely=.2, anchor="c", bordermode=OUTSIDE)

            self.login_label.place(relx=.5, rely=0.3, anchor="c")
            self.login_entry.place(relx=.5, rely=0.35, anchor="c")

            self.email_label.place(relx=.5, rely=0.4, anchor="c")
            self.email_entry.place(relx=.5, rely=0.45, anchor="c")

            self.name_label.place(relx=.5, rely=0.5, anchor="c")
            self.name_entry.place(relx=.5, rely=0.55, anchor="c")

            self.password_label.place(relx=.5, rely=0.6, anchor="c")
            self.password_entry.place(relx=.5, rely=0.65, anchor="c")

        self.visible = not self.visible
