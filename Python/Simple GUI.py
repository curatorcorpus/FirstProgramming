#simple GUI

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title('Age Calculator')
root.geometry('400x500')

app = Frame(root)
app.grid()
button1 = Button(app, text = "Calculate Age")
button1.grid()

#kick off the event loop
root.mainloop() 
 
