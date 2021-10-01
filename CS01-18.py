from tkinter import *
root = Tk()
root.title('My name')
Text = Label(text='My name is',fg='blue',font=24).grid(row=0,column=0)
Text = Label(text='Tanakorn',fg='orange',font=24).grid(row=1,column=1)
Text = Label(text='Khuntamanee',fg='green',font=24).grid(row=2,column=2)
root.geometry('500x250')
root.mainloop()