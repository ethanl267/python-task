from tkinter import *

root = Tk()
root.title("Authentification")
root.geometry("500x500")


label1=Label(root, text="please enter login details" , width=20 ,  font=10).place(x=170 , y=10)

label2=Label(root, text="username" , width=20 ,  font=10).place(x=170 , y=100)
entry2=Entry(root, width=20).place(x=110, y=150)

label3=Label(root, text="password" , width=20 ,  font=10).place(x=170 , y=180)
entry3=Entry(root, width=20).place()

btn=Button(root, text="login" , width=20).place(x=180 , y=300)

root.mainloop()