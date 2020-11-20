from tkinter import messagebox
from tkinter import *
import requests




root=Tk()
root.title("My Weather App")
root.geometry("500x450")
def clear():
    city_entry.delete(0, END)


def myweather():
    mycity=city_entry.get()
    key='ae088606657a7537989abe91de3934d9'
    url='http://api.openweathermap.org/data/2.5/weather'
    parameters= {'appid': key, 'q': mycity, 'units':'Metric'}
    result=requests.get(url, parameters)
    result1=result.json()
    location_out.config(text=str(result1['sys']['country']))
    temp_out.config(text=str(result1['main']['temp']))
    windsd_out.config(text=str(result1['wind']))
    humid_out.config(text=str(result1['main']['humidity']))
    cloudcover_out.config(text=str(result1['clouds']))
    print(result1)




city_text=StringVar()
city_entry=Entry(root, textvariable=city_text)
city_entry.pack()

btn=Button(root, text="search weather", fg="black", bg="red",  width=12, command=lambda :myweather()).place(x=190 , y=30)



location_lbl = Label(root, text="location", font=('bold', 15)).place(x=10, y=90)
location_out= Label(root, text="location", font=('bold', 15))
location_out.place(x=100, y=90)

temp_lbl = Label(root, text="temperature ", font=('bold', 15)).place(x=10, y=135)
temp_out= Label(root, text="temperature", font=('bold', 15))
temp_out.place(x=150, y=135)

windsd_lbl = Label(root, text="windspeed", font=('bold', 15)).place(x=10, y=190)
windsd_out= Label(root, text="windspeed", font=('bold', 15))
windsd_out.place(x=130, y=190)

humidity_lbl = Label(root, text="humidity", font=('bold', 15)).place(x=10, y=250)
humid_out= Label(root, text="humidity", font=('bold', 15))
humid_out.place(x=120, y=250)

cloudcover_lbl = Label(root, text="cloudcover", font=('bold', 15)).place(x=10, y=300)
cloudcover_out= Label(root, text="cloudcover", font=('bold', 15))
cloudcover_out.place(x=130, y=300)

extbtn=Button(root, text='exit', fg="yellow", bg="black", command=exit).place(x=150 , y=350)
clearbtn=Button(root, text="clear", fg="blue", bg="skyblue", command=clear).place(x=200 , y=350)

root.mainloop()