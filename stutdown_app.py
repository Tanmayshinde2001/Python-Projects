from tkinter import *
import os
from tkinter.font import BOLD

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("stutdown app")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st,text="Restart",font=("Times New Roman",30,BOLD),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=40,width=150)

rt_button = Button(st,text="Restart time",font=("Times New Roman",30,BOLD),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=140,y=120,height=40,width=220)

st_button = Button(st,text="Shut Down",font=("Times New Roman",30,BOLD),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=140,y=180,height=40,width=180)

st.mainloop()