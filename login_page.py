from tkinter import *
import customtkinter
from PIL import Image,ImageTk
customtkinter.set_appearance_mode("light")
i= 0

def change_mode():
    global i
    if i== 0:
        customtkinter.set_appearance_mode("dark")
        mode_btn.configure(image=light_mode)
        i = i+1
    elif i == 1:
        customtkinter.set_appearance_mode("light")
        mode_btn.configure(image=dark_mode)
        i = i-1

def sign_in():
     
    name = username.get()
    code = password.get()
    if name == "User Name" or code == "Password":
        error = customtkinter.CTkToplevel(window)
        error.geometry("300x150+500+250")
        error.title("Error")
        error.wm_iconbitmap("icon.ico")
        frame = customtkinter.CTkFrame(error)
        frame.pack(fill="both",expand="true",padx=10,pady=15)
        label = customtkinter.CTkLabel(frame,text="Please enter your\ncredentials first",font=("Consolas",20,"bold"))
        label.pack(side="top",pady=15)
        customtkinter.CTkButton(frame,text="OK",fg_color="#2b52ff",command=lambda:error.destroy()).pack(side="top")



def enter_user(event):
    username.configure(width=270)
    username.place(x=540)

def leave_user(event):
    username.configure(width=250)
    username.place(x=550)
    
def enter_pass(event):
    password.configure(width=270)
    password.place(x=540)

def leave_pass(event):
    password.configure(width=250)
    password.place(x=550)
    
def user_enter(e):
    name = username.get()
    if name == "" or name == "User Name":
        username.delete(0,END)

def user_leave(e):
    name = username.get()
    if name == '':
        username.insert(0,"User Name")

def pass_enter(e):
    name = password.get()
    if name == "" or name == "Password":
        password.delete(0,END)

def pass_leave(e):
    name = password.get()
    if name == '':
        password.insert(0,"Password")
    

window = customtkinter.CTk()
window.geometry("880x500")
window.title("Library Management")
window.wm_iconbitmap("icon.ico")
window.wm_attributes('-transparentcolor','#faf8f2')
my_image = customtkinter.CTkImage(light_image=Image.open("login.png"),size=(400, 450))

image_label = customtkinter.CTkLabel(window,image=my_image,text="")
image_label.pack(side="left",padx=40)

textlabel = customtkinter.CTkLabel(window,text="Welcome to the\nCity Library",font=("Consolas",24,"bold"))
textlabel.place(x=580,y=70)

light_mode = customtkinter.CTkImage(light_image=Image.open("lightmode.png"),size=(50,50))
dark_mode = customtkinter.CTkImage(light_image=Image.open("darkmode.png"),size=(50,50))

mode_btn = customtkinter.CTkButton(window,height=60,text="",fg_color="transparent",hover_color="",width=60,image=light_mode,command=change_mode)
mode_btn.place(x=790,y=10)

username = customtkinter.CTkEntry(window,height=35,width=250,justify="center",border_color="#fff",border_width=0,font=("Cascadia",18))
username.place(x=550,y=150)
username.insert(0,"User Name")
username.bind('<FocusIn>',user_enter)
username.bind('<FocusOut>',user_leave)
username.bind('<Enter>',enter_user)
username.bind('<Leave>',leave_user)

password = customtkinter.CTkEntry(window,height=35,width=250,justify="center",border_width=0,border_color="#fff",font=("Cascadia",18))
password.place(x=550,y=200)
password.insert(0,"Password")
password.bind('<FocusIn>',pass_enter)
password.bind('<FocusOut>',pass_leave)
password.bind('<Enter>',enter_pass)
password.bind('<Leave>',leave_pass)

# window.bind('<Return>',sign_in)

sign_in_btn = customtkinter.CTkButton(window,text="Sign in",height=30,fg_color="#2b52ff",width=250,text_color="#fff",command=sign_in)
sign_in_btn.place(x=550,y=250)

signup_btn = customtkinter.CTkButton(window,text="Sign Up",fg_color="transparent",hover_color="",text_color="#2b52ff")
signup_btn.place(x=660,y=305)
signup_label = customtkinter.CTkLabel(window,text="Don't have an account?")
signup_label.place(x=570,y=305)


window.mainloop()