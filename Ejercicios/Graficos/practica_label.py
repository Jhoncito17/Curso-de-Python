from tkinter import *
root=Tk()

miframe=Frame(root,width=500,height=400)
miframe.pack()


Label(miframe,text="Hola gente de python",fg="red",font=("Comic sans MS",18)).place(x=100,y=200)


root.mainloop()