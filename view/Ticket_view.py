from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from model.validator.ticket_validator import *


def save_btn_click():
    errors=[]

    person = (id.get(),ticket_code.get(),source.get(),destination.get(),airline.get(),start_date_time.get(),end_date_time.get(),
              price.get(),seat_no.get(),sold.get())


    if code_validator(ticket_code.get()):
        errors.append('invalid code')

    if not source_validator(source.get()):
        errors.append('invalid source')

    if not destination_validator(destination.get()):
        errors.append('invalid destination')

    if not airline_validator(airline.get()):
        errors.append('invalid airline')

    if start_date_time_validator(start_date_time.get()):
        errors.append('invalid date')

    if end_date_time_validator(end_date_time.get()):
        errors.append('invalid date')

    if price_validator(price.get()):
        errors.append('invalid price')

    if seat_no_validator(seat_no.get()):
        errors.append('invalid seat no')


    if errors:
        msg.showerror('Error',errors)
    else:
        msg.showinfo('Success','informations saved')
        table.insert('', END, values=person)
        reset_form()




def reset_form():
    id.set(id.get()+1)
    ticket_code.set(0)
    source.set("")
    destination.set("")
    airline.set("")
    start_date_time.set("")
    end_date_time.set("")
    price.set(0)
    seat_no.set(0)
    sold.set(False)




def clear_btn():
    for row in table.get_children():
        table.delete(row)




window = Tk()
window.geometry("1330x600")
window.title('Ticket info')




#Id
Label(window,text='id').place(x=50,y=20)
id=IntVar(value=1)
Entry(window,textvariable=id,state='readonly').place(x=100,y=20)

#ticket_code
Label(window,text='ticket code').place(x=25,y=60)
ticket_code=IntVar(value=0)
Entry(window,textvariable=ticket_code,).place(x=100,y=60)


#source
Label(window,text='source').place(x=40,y=100)
source=StringVar()
ttk.Combobox(window,values=['Tehran','Shiraz','Esfahan','Kish','Mashhad','Qeshm'],state='readonly').place(x=100,y=100)


#destination
Label(window,text='destination').place(x=20,y=140)
destination=StringVar()
ttk.Combobox(window,values=['Tehran','Shiraz','Esfahan','Kish','Mashhad','Qeshm'],state='readonly').place(x=100,y=140)


#airline
Label(window,text='airline').place(x=35,y=180)
airline=StringVar()
ttk.Combobox(window,values=['Qeshm air','Aseman','Mahan air','Iran air','Meraj','Kish airline'],state='readonly').place(x=100,y=180)

#start_date_time
Label(window,text='start date time').place(x=13,y=220)
start_date_time=StringVar(value='0000/00/00')
Entry(window,textvariable=start_date_time).place(x=100,y=220)


#end_date_time
Label(window,text='end date time').place(x=13,y=260)
end_date_time=StringVar(value='0000/00/00')
Entry(window,textvariable=end_date_time).place(x=100,y=260)


#price
Label(window,text='price').place(x=35,y=300)
price=IntVar()
Entry(window,textvariable=price).place(x=100,y=300)

#TODO
#seat_no
Label(window,text='seat no').place(x=35,y=340)
seat_no=IntVar(value=0)
ttk.Combobox(window,values=['','']).place(x=100,y=340)

#sold
Label(window,text='sold').place(x=35,y=380)
sold=BooleanVar(value= False)
ttk.Combobox(window,values=['Yes','No'],state='readonly').place(x=100,y=380)


#todo
#date
Label(window,text='date').place(x=365,y=380)
date=StringVar()
ttk.Combobox(window,values=['','',''],state='readonly').place(x=400,y=380)

#todo
#city
Label(window,text='city').place(x=600,y=380)
city=StringVar()
ttk.Combobox(window,values=['','',''],state='readonly').place(x=635,y=380)







table=ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8,9],show='headings')
table.place(x=270,y=20)


table.heading(1, text='id')
table.heading(2, text='ticket code')
table.heading(3, text='source')
table.heading(4, text='destination')
table.heading(5, text='start date time')
table.heading(6, text='end date time')
table.heading(7, text='price')
table.heading(8, text='seat no')
table.heading(9, text='sold')



table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=130)
table.column(4, width=130)
table.column(5, width=130)
table.column(6, width=130)
table.column(7, width=110)
table.column(8, width=110)
table.column(9, width=110)






Button(window,text='Save',command=save_btn_click).place(x=70,y=500,width=80)
Button(window,text='Clear',command=clear_btn).place(x=170,y=500,width=80)








window.mainloop()