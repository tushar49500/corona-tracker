from tkinter import *
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url)
Soup = BeautifulSoup(page.content, "html.parser")
info = Soup.find_all(class_="maincounter-number")
a = [items.get_text() for items in info]

country=" "

root = Tk()
root.title("corona tracker")
root.geometry("1000x1000")
root.configure(bg="black")
font = ("helvetica", 15, "bold")


def find_info():
    country = c.get()
    url1 = "https://www.worldometers.info/coronavirus/country/" + country
    page1=requests.get(url1)
    Soup1=BeautifulSoup(page1.content, "html.parser")
    info1=Soup1.find_all(class_="maincounter-number")
    b=[items.get_text() for items in info1]

    label1=Label(root, font=font, text="Total Cases of Corona Virus in " + country,bg="red")
    label1.pack()
    label1=Label(root, font=font,bg="red", text=b[0])
    label1.pack()
    label1=Label(root, font=font, text="Total Deaths in " + country,bg="orange")
    label1.pack()
    label1=Label(root, font=font,bg="orange",text=b[1])
    label1.pack()
    label1=Label(root, font=font, text="Total Recovered people in " + country,bg="green")
    label1.pack()
    label1=Label(root, font=font,bg="green",text=b[2])
    label1.pack()

label1=Label(root, font=font, bg="red", text="Total Cases of Corona Virus ")
label1.pack()
label1=Label(root, font=font,bg="red",text=a[0])
label1.pack()
label1=Label(root, font=font,bg="orange", text="Total Deaths")
label1.pack()
label1=Label(root, font=font,bg="orange", text=a[1])
label1.pack()
label1=Label(root, font=font,bg="green", text="Total Recovered People")
label1.pack()
label1=Label(root, font=font,bg="green", text=a[2])
label1.pack()
label1=Label(root, font=font,bg="silver",text="Please Enter Country Name For Cases")
label1.pack()
c= Entry(root, font=font)
c.pack()
button1 =Button(root, font=font, text="find info", bg="yellow", command=find_info)
button1.pack()

root.mainloop()
