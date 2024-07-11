from tkinter import *
from random import randint
from PIL import Image, ImageTk

# frame
root = Tk()
root.geometry("500x500")
root.title('Random Password Gen')
root.configure(bg='black')
root.iconbitmap("C:/Users/haash/OneDrive/Pictures/incognito_icon.ico")


def click_pass():
    # logic for random password
    function_pass = ""

    for i in range(3):
        i = chr(randint(65, 90))
        for j in range(1):
            j = chr(randint(65, 90)).lower()
            for h in range(1):
                h = str(randint(1, 10))
                function_pass = str(function_pass) + i + j + h
                password.set(function_pass)

# Password String Variable
password = StringVar()

# Title
title = Label(root, text="Random Password Generator!", font=("Calibri", 20, "bold"), bg='black', fg='green')
title.place(relx=.5, rely=.1, anchor="center")

# Password Button
pass_button = Button(root, text="Random Password", font=("Helvetica", 18, "bold"), padx=75, pady=40, bg="black",
                     fg="green", command=click_pass)
pass_button.place(relx=.5, rely=.4, anchor="center")

# Password Label
pass_label = Label(root, textvariable=password, font=("Calibri", 17, "bold"), bg='black', fg='green')
pass_label.place(relx=.5, rely=.62, anchor="center")

# Cool Mask Guy Image
old_img = Image.open("C:/Users/haash/OneDrive/Pictures/incognito_guy.png")
new_img = old_img.resize((200, 200))
img = ImageTk.PhotoImage(new_img)
img_label = Label(root, image=img, bg='black')
img_label.place(relx=.5, rely=.87, anchor="center")


root.mainloop()
