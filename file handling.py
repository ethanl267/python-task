from tkinter import *

root = Tk()
root.title('my GUI')
root.geometry("1000x500")


def create_txt():
    text_file = open("sample.txt", 'w+')
    stuff = text_file.read()
    text_file.close()



def dsiplay_txt():
    text_file = open('sample.txt', 'r')
    my_text.insert(END, text_file.read())
    text_file.close()

def append_txt():
    text_file = open('sample.txt', 'a')
    my_text.insert(END, text_file.read() )
    text_file.close()

def clear_txt():
     text_file = open('sample.txt', '')
     my_text.delete(END, text_file.read())
     text_file.close()


def exit_txt():
    text_file = open('sample.txt', 'a')
    my_text.insert(END, text_file.read() )
    text_file.close()





my_text = Text(root, width=40, height=10)

lable1 = Label(root, text="My weekend activities", font="200").place(x=70, y=60)

btn1 = Button(root, text="create textflie", width=20, command=create_txt)

btn2 = Button(root, text="display textfile", width=20, command=dsiplay_txt)

btn3 = Button(root, text="append data", width=20, command=append_txt)

btn4 = Button(root, text="clear textflie", width=20, command=clear_txt)

btn5 = Button(root, text="exit", width=20, command=exit_txt)


my_text.place(x=50, y=200)
btn1.place(x=10, y=400)
btn2.place(x=200, y=400)
btn3.place(x=400, y=400)
btn4.place(x=600, y=400)
btn5.place(x=800, y=400)


root.mainloop()
