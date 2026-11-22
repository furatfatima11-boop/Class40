from tkinter import *
root = Tk()
root.title("Demo Window")
root.geometry('400x400')
lbl = Label(text="Please Fill Out The Form!",fg="black",bg="pink",height= 3,width= 30,padx= 20,pady = 15)
name_lbl = Label(text="Full Name:",bg="pink")
name_entry = Entry()
date_lbl = Label(text="Date Of Birth:", bg="pink")
date_entry = Entry()
country_lbl = Label(text="Birth Place:", bg="pink")
country_entry = Entry()
state_lbl = Label(text="State/Provice of residency:", bg="pink")
state_entry = Entry()
def display():
    name = name_entry.get()
    date = date_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    global message 
    message = "Thank You For Filling Out This Form!\n"
    greet = "Hello "+name+"\n"
    date = "You were born on "+date+"\n"
    country = "You were born in "+country+"\n"
    state = "You currently live in "+state+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date)
    text_box.insert(END, country)
    text_box.insert(END, state)
text_box = Text(height =7)
btn = Button(text = "Submit",command=display,height = 1,bg="pink",fg="black")
name_lbl.pack()
name_entry.pack()
date_lbl.pack()
date_entry.pack()
country_lbl.pack()
country_entry.pack()
state_lbl.pack()
state_entry.pack()
text_box.pack()
btn.pack()
root.mainloop()