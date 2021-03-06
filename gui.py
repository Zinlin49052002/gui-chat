from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Whisper")
root.geometry("1600x800+0+0")

fg = "#ffffff"
bg = "#333333"
font=('aril',14,'bold')
t=StringVar()
t1=StringVar()
user=StringVar()
pwa=StringVar()
repwa=StringVar()
ems=StringVar()


logo_icon=ImageTk.PhotoImage(file="icons/user6.png",)
user_icon=ImageTk.PhotoImage(file="icons/user2.png")
mail_icon=ImageTk.PhotoImage(file="icons/mail.png")
pass_icon=ImageTk.PhotoImage(file="icons/lock1.png")
logo_icon=ImageTk.PhotoImage(file="icons/user7.png")
addr_icon=ImageTk.PhotoImage(file="icons/addr.png")

co_icon=ImageTk.PhotoImage(file="icons/cop.png")
ph_icon=ImageTk.PhotoImage(file="icons/ph.png")

root.config(background=bg)



def changeFrame(old,new):
    old.destroy()
    new()

def loginFrame():
    lf = Frame(root,bg='#333333',bd=0,width=800,height=800,relief="solid")
    lf.config(highlightcolor="#FFA500",highlightbackground="#FFA500",highlightthickness=3)

    intro=Label(lf,text='Whisper',font=font,padx=150,pady=20,bg=bg,fg="#FFA500")

    username = Entry(lf,width=26,font=5,textvariable=t,fg="gray")
    t.set("Type Username")

    password = Entry(lf,width=26,font=5,textvariable=t1,fg="gray")
    t1.set("Type Password")
    loginButton = Button(lf,text="Login",relief="flat",padx=22,bg=bg,fg="#FFA500")
    signupButton = Button(lf,text="Signup",relief="flat",padx=18,bg=bg,fg="#FFA500",command=lambda : changeFrame(lf,signupFrame))
    padlabel=Label(lf)
    intro.grid(row=0,column=1)
    username.grid(row=1,column=0,columnspan=4,padx=30,pady=20)
    password.grid(row=2,column=0,columnspan=4,pady=20)
    loginButton.grid(row=3,column=1,columnspan=2,padx=20)
    signupButton.grid(row=4,column=1,columnspan=2,pady=30)
    
    padlabel.grid(row=5,column=1,pady=200)
    lf.pack(anchor="center",pady=200)

def signupFrame():
    sf = Frame(root,bg='#333333',bd=0,relief="solid")
    sf.config(highlightcolor="#FFA500",highlightbackground="#FFA500",highlightthickness=3)
    Logo=Label(sf,text='Sign Up',font=font,padx=150,pady=20,bg=bg,fg="#FFA500")
    usericon=Label(sf,image=user_icon,compound=LEFT,bg="#333333")
    username = Entry(sf,width=26,font=5,textvariable=user,fg="gray")
    user.set("Username")
    mailicon=Label(sf,image=mail_icon,compound=LEFT,bg="#333333")
    password = Entry(sf,width=26,font=5,textvariable=pwa,fg="gray")
    pwa.set("Password ")
    rePassword = Entry(sf,width=26,font=5,textvariable=repwa,fg="gray")
    repwa.set("Repassword")
    email = Entry(sf,width=26,font=5,textvariable=ems,fg="gray")
    ems.set("Email")
    signupButton = Button(sf,text="Signup",relief="flat",padx=18,bg=bg,fg="#FFA500")
    backButton = Button(sf,text="Back",relief="flat",padx=24,bg=bg,fg="#FFA500",command=lambda : changeFrame(sf,loginFrame))
    labpad=Label(sf,bg="#333333")
    Logo.grid(row=0,column=0,columnspan=4)
    usericon.grid(row=1,column=0,columnspan=4,padx=10,sticky='w')
    mailicon.grid(row=2,column=0,columnspan=4,padx=10,sticky='w')

    username.grid(row=1,column=0,columnspan=4)
    password.grid(row=2,column=0,columnspan=4,pady=30)
    rePassword.grid(row=3,column=0,columnspan=4)
    email.grid(row=4,column=0,columnspan=4,pady=30)
    signupButton.grid(row=5,column=1,columnspan=2)
    backButton.grid(row=6,column=1,columnspan=2,pady=30)
    labpad.grid(row=7,column=1,pady=20)
    sf.pack(anchor="center",pady=200)

loginFrame()

root.mainloop()