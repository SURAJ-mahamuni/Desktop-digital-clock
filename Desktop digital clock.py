from tkinter import *
from datetime import date
import time
curr = time.time()
today1=date.today()
cctime=time.ctime(curr)

def update():
    hour=time.strftime("%I")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    pm_am=time.strftime("%p")
    week=time.strftime("%A")
    date_number=time.strftime("%d")
    month_name=time.strftime("%B")
    label1.config(text=hour + ":" + minute + ":" + pm_am)

    label2.config(text=week + " , " + date_number+" " + month_name)
    

    label1.after(1000,update)

root=Tk()
root.title("Date & Time")
root.geometry("430x300+650+10")
root.overrideredirect(True)

label1=Label(root,text="",bg="blue",fg="#13EDF4")
Font_tuple = ("arial",60,"bold")
label1.configure(font=Font_tuple)
label1.grid(row=0,column=0,padx=5,pady=5)
label1.after(1000,update)


label2=Label(root,text="",bg="blue",fg="#F9EF5A")
Font_tuple1 = ("arial",30,"bold")
label2.configure(font=Font_tuple1)
label2.grid(row=1,column=0,padx=5,pady=5)
root.configure(bg='blue')

label3=Label(root,text="SURAJ_mahamuni",bg="blue",fg="#F9EF5A")
Font_tuple1 = ("arial",10,"bold")
label3.configure(font=Font_tuple1)
label3.grid(row=2,column=0,padx=5,pady=5)
root.configure(bg='blue')


root.wm_attributes('-transparentcolor', 'blue')
# root.wm_attributes('-transparentcolor', 'white')
root.mainloop()
