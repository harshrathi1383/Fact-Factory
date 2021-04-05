from tkinter import *
from tkinter import messagebox
from time import sleep
from PIL import Image
from win10toast import ToastNotifier
import random
root = Tk() #This creates a main GUI window for user interaction with application.
root.iconbitmap('icon1.ico') #icon which apperas in window created by program.
root.title("Welcome to the fact notifier application") #title of main window.
root.geometry("370x600") #dimension of mina window.
heading = Label(root, text='Select your interests!') 
heading.grid(row=0, column=0)
size = (300, 45)
interests = [] #This stores the interests of the user.
for i in range(8):
    interests.append(IntVar())
#This opens the image of every interest provided by the application and resize them to given dimension.
for i in range(8):
    img = Image.open(r"img"+str(i)+".png")
    r_img = img.resize(size)
    r_img.save("img" + str(i) + ".png")
#Image of every interest is stored in variable of type which can be attached to GUI.
img0 = PhotoImage(file='img.png')
img1 = PhotoImage(file='img1.png')
img2 = PhotoImage(file='img2.png')
img3 = PhotoImage(file='img3.png')
img4 = PhotoImage(file='img4.png')
img5 = PhotoImage(file='img5.png')
img6 = PhotoImage(file='img6.png')
img7 = PhotoImage(file='img7.png')
#check buttons are created for every interests
c0 = Checkbutton(root, image=img0, variable=interests[0])
c0.grid(row=1, sticky=W)
c1 = Checkbutton(root, image=img1, variable=interests[1])
c1.grid(row=2, sticky=W)
c2 = Checkbutton(root, image=img2, variable=interests[2])
c2.grid(row=3, sticky=W)
c3 = Checkbutton(root, image=img3, variable=interests[3])
c3.grid(row=4, sticky=W)
c4 = Checkbutton(root, image=img4, variable=interests[4])
c4.grid(row=5, sticky=W)
c5 = Checkbutton(root, image=img5, variable=interests[5])
c5.grid(row=6, sticky=W)
c6 = Checkbutton(root, image=img6, variable=interests[6])
c6.grid(row=7, sticky=W)
c7 = Checkbutton(root, image=img7, variable=interests[7])
c7.grid(row=8, sticky=W)
#Ask the user to enter the time interval
Label(root, text="ENTER THE TIME INTERVAL(in mins):").grid(row=9, sticky=W)
timeInterval = Entry(root)
timeInterval.grid(row=9, column=0, sticky=E)
flag = 0
def notifier(facts, i):
    """This method created the ToastNotifier object and select the interest from the list and produces the notification and show it to the user """
    if i == len(facts):
        return
    obj = ToastNotifier()
    obj.show_toast("Facts", facts[i], duration=8,
                   threaded=True, icon_path="icon1.ico")
    timeInSec = eval(timeInterval.get())
    timeInSec *= 60
    timeInSec *= 1000
    root.after(timeInSec, lambda: notifier(facts, i+1)) #This creates the next notification after the time interval given by the user.

def getStarted(child):
    """This function starts the process of creating fact notifications after every time interval selected by user"""
    child.destroy()
    Label(root, text="You are receiving facts notifications.").grid()
    Label(root, text="Press Stop to stop the service").grid()
    facts = []
    for i in range(len(interests)):
        factfile = None
        if (interests[i].get() == 1):
            if (i == 0):
                factfile = open('history.txt', 'r')
            if i == 1:
                factfile = open('sports.txt', 'r')
            if i == 2:
                factfile = open('food.txt', 'r')
            if i == 3:
                factfile = open('science.txt', 'r')
            if i == 4:
                factfile = open('space.txt', 'r')
            if i == 5:
                factfile = open('maths.txt', 'r')
            if i == 6:
                factfile = open('technology.txt', 'r')
            if i == 7:
                factfile = open('coding.txt', 'r')
        if factfile is None:
            continue
        for line in factfile:
            facts.append(line)
        factfile.close()
    random.shuffle(facts)
    #     root.after(5000,check)
    notifier(facts, 0)
    # root.config(state="normal")


def start():
    """This function creates the child window which shows the user the interest selected by them and ask for permission to get started with notification"""
    global flag
    child = Tk()
    child.iconbitmap('icon1.ico')
    child.title("Interests")
    Label(child, text="You will be receiving fact notifications every " +
          str(timeInterval.get())+" minutes on topics:").grid()
    if len(timeInterval.get()) == 0 or (timeInterval.get()).isnumeric() == False:
        messagebox.showerror(
            "Non valid", "Please enter the valid time interval.")
        # Button(child, text="close", command=child.destroy).grid()
        child.destroy()
        flag = 0
        return
    i = 1
    #Put interests of user on child window
    if interests[0].get() == 1:
        Label(child, text=str(i) + ". History").grid()
        i += 1
    if interests[1].get() == 1:
        Label(child, text=str(i) + ". Sports").grid()
        i += 1
    if interests[2].get() == 1:
        Label(child, text=str(i) + ". food").grid()
        i += 1
    if interests[3].get() == 1:
        Label(child, text=str(i) + ". Science").grid()
        i += 1
    if interests[4].get() == 1:
        Label(child, text=str(i) + ". Space").grid()
        i += 1
    if interests[5].get() == 1:
        Label(child, text=str(i) + ". Maths").grid()
        i += 1
    if interests[6].get() == 1:
        Label(child, text=str(i) + ". Technology").grid()
        i += 1
    if interests[7].get() == 1:
        Label(child, text=str(i) + ". Coding").grid()
        i += 1
    if (i == 1):
        #show error message if user has not selected any interest
        messagebox.showerror(
            "Non-valid request", "You haven't selected any interest of yours.Please select.")
        child.destroy()
        # Button(child, text="close", command=child.destroy).grid()
        # time.sleep(4)
        # root.destroy()
        flag = 0
    else:
        Label(child, text="Have a great day!").grid()
        Button(child, text="Get started", borderwidth=4,
               highlightthickness=5, command=lambda: getStarted(child)).grid()
        # root.quit()

#start button
button = Button(root, text="Start", bg="#3CB371", command=start)
button.grid()


def quit():
    """This is the function which stops the application from creating further notifications and closes the application"""
    messagebox.showinfo(
        "Facts Notifier", "Success \n You will not receive notifications anymore.")
    root.destroy()

#stop and quit button
Button(root, text="Stop and quit", bg='red', command=quit).grid()
root.mainloop()
