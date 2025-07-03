from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from model.validator.user_validator import *


def save_btn_click():
    errors=[]

    person = (id.get(),name.get(),family.get(),birthday.get(),username.get(),'*'*len(password.get()),locked.get(),role.get())

    if not en_name_validator(name.get()):
        errors.append('invalid name')

    if not en_family_validator(family.get()):
        errors.append('invalid family')

    if not birthday_validator(birthday.get()):
        errors.append('invalid birthday')

    if not username_validator(username.get()):
        errors.append('invalid username')

    if not password_validator(password.get()):
        errors.append('invalid password')

    if not role_validator(role.get()):
        errors.append('invalid role')

    if errors:
        msg.showerror('Error',errors)
    else:
        msg.showinfo('Success','informations saved')
        table.insert('',END,values=person)
        reset_form()




def reset_form():
    id.set(id.get()+1)
    name.set("")
    family.set("")
    birthday.set(0)
    username.set("")
    password.set("")
    locked.set(False)
    role.set("")




def clear_btn():
    for row in table.get_children():
        table.delete(row)




window = Tk()
window.geometry("1200x500")
window.title('personal info')




#Id
Label(window,text='id').place(x=50,y=20)
id=IntVar(value=1)
Entry(window,textvariable=id,state='readonly').place(x=100,y=20)

#Name
Label(window,text='name').place(x=40,y=60)
name=StringVar()
Entry(window,textvariable=name).place(x=100,y=60)

#Family
Label(window,text='family').place(x=40,y=100)
family=StringVar()
Entry(window,textvariable=family).place(x=100,y=100)


#birthday
Label(window,text='birthday').place(x=35,y=140)
birthday=StringVar(value='0000/00/00')
Entry(window,textvariable=birthday).place(x=100,y=140)

#username
Label(window,text='username').place(x=35,y=180)
username=StringVar(value='')
Entry(window,textvariable=username).place(x=100,y=180)


#password
Label(window,text='password').place(x=35,y=220)
password=StringVar(value='')
Entry(window,textvariable=password,show='*').place(x=100,y=220)


#todo
#locked
Label(window,text='locked').place(x=35,y=260)
locked=BooleanVar()
Entry(window,textvariable=locked).place(x=100,y=260)

#role
Label(window,text='role').place(x=35,y=300)
role=StringVar(value='User')
ttk.Combobox(window,textvariable=role,values=['User','Admin'],state='readonly').place(x=100,y=300)




table=ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8],show='headings')
table.place(x=270,y=20)


table.heading(1, text='id')
table.heading(2, text='name')
table.heading(3, text='family')
table.heading(4, text='birthday')
table.heading(5, text='username')
table.heading(6, text='password')
table.heading(7, text='locked')
table.heading(8, text='role')



table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=130)
table.column(4, width=130)
table.column(5, width=130)
table.column(6, width=130)
table.column(7, width=110)
table.column(8, width=110)






Button(window,text='Save',command=save_btn_click).place(x=70,y=400,width=80)
Button(window,text='Clear',command=clear_btn).place(x=170,y=400,width=80)








window.mainloop()