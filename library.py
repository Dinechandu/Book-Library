from tkinter import  *
import backend

window=Tk()

def get_selected_row(event):
     try:
        global selected_list
        index=listbox.curselection()[0]
        selected_list=listbox.get(index)
        t1.delete(0,END)
        t1.insert(END,selected_list[1])
        t2.delete(0,END)
        t2.insert(END,selected_list[2])
        t3.delete(0,END)
        t3.insert(END,selected_list[3])
        t4.delete(0,END)
        t4.insert(END,selected_list[4])
     except IndexError:
        pass
    

def view_all():
    listbox.delete(0,END)
    for row in backend.View():
        listbox.insert(END,row)

def search_entry():
    listbox.delete(0,END)
    for row in backend.Search(title.get(),author.get(),year.get(),isbn.get()):
        listbox.insert(END,row)

def add_entry():
    backend.Insert(title.get(),author.get(),year.get(),isbn.get())
    listbox.delete(0,END)
    listbox.insert(END,title.get(),author.get(),year.get(),isbn.get())
        
def delete_entry():
    backend.Delete(selected_list[0])
    
def update_entry():
    backend.Update(selected_list[0],title.get(),author.get(),year.get(),isbn.get())

# LABELS Declaration
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#EntryBox Declaration
title=StringVar()
t1=Entry(window,width=20,textvariable=title)
t1.grid(row=0,column=1)

author=StringVar()
t2=Entry(window,width=20,textvariable=author)
t2.grid(row=0,column=3)

year=StringVar()
t3=Entry(window,width=20,textvariable=year)
t3.grid(row=1,column=1)

isbn=StringVar()
t4=Entry(window,width=20,textvariable=isbn)
t4.grid(row=1,column=3)

#ListBox declaration
listbox=Listbox(window,height=6,width=40)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

#ScrollBar Declaration
scrl=Scrollbar(window)
scrl.grid(row=2,column=2,rowspan=6)

#Configuring ScrollBar with ListBox
listbox.config(yscrollcommand=scrl.set)
scrl.config(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',get_selected_row)

# Button Declaration
b1=Button(window,text="View All",width=18,command=view_all)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=18,command=search_entry)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=18,command=add_entry)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Entry",width=18,command=update_entry)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=18,command=delete_entry)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=18,command=window.quit)
b6.grid(row=7,column=3)



window.mainloop()

