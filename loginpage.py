from tkinter import *

root = Tk()
root.title("Login Application")

def submit():
    password_show = f"Your Password is : {password.get()}"
    username_show = f"Your Username is : {username.get()}"

    lp =  Label(text=password_show)
    lp.config(font=("Arial", 16))

    lp2 =  Label(text=username_show)
    lp2.config(font=("Arial", 16))

    lp2.grid(row=5,column=0)
    lp.grid(row=6,column=0)

l2 = Label(root, text="username:")
l2.config(font=("Arial", 14))

l3 = Label(root, text="password:")
l3.config(font=("Arial", 14))

username = StringVar()
password = StringVar()

e1 = Entry(root, textvariable=username)
e2 = Entry(root, textvariable=password, show="*")

login_button = Button(root, text="SUBMIT",command=submit)
login_button.config(font=("Arial", 12))

l2.grid(row=0, column=0)
e1.grid(row=0, column=1)

l3.grid(row=1, column=0)
e2.grid(row=1, column=1)

login_button.grid(row=4, column=0)

root.mainloop()
