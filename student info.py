from tkinter import *

root=Tk()
root.geometry("600x600")
root.title("student info")


label1 = Label(root, text="student info" , width=20 , font=("bold", 20))
label1.place(x=80 , y=53)

label2 = Label(root, text='Fullname', width=20 , font=("bold, 10"))
label2.place(x=80, y=130)
entry2=Entry(root)
entry2.place(x=240 , y=130)

label3 = Label(root, text='email', width=20 , font=("bold, 10"))
label3.place(x=68, y=180)
entry3=Entry(root)
entry3.place(x=240, y=180)

label4 = Label(root, text='select school', width=20 , font=("bold, 10"))
label4.place(x=70, y=280)

list = ['rocklands', 'mondale']
s=StringVar()
droplist=OptionMenu(root,s, list)
droplist.config(width=15)
s.set("select your school")
droplist.place(x=240 , y=280)

button=Button(root, text="Submit" , width=20 , bg='brown', fg='white').place(x=180, y=380)

root.mainloop()