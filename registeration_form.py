from tkinter import *
import customtkinter
from PIL import Image
import ast
customtkinter.set_appearance_mode("light")

#defining all the images required in the app
# ======================================================================================================================
light_mode = customtkinter.CTkImage(light_image=Image.open("lightmode.png"),size=(50,50))
dark_mode = customtkinter.CTkImage(light_image=Image.open("darkmode.png"),size=(50,50))
login_image = customtkinter.CTkImage(light_image=Image.open("login.png"),size=(450, 500))
signup_image = customtkinter.CTkImage(light_image=Image.open("signup.png"),size=(440,450))
warning_image = customtkinter.CTkImage(light_image=Image.open("warning-sign.png"),size=(30,30))
success_image = customtkinter.CTkImage(light_image=Image.open("successful.png"),size=(30,30))
issue_book = customtkinter.CTkImage(light_image=Image.open("issue_book.png"),size=(270,310))
add_book = customtkinter.CTkImage(light_image=Image.open("add_book.png"),size=(270,320))
return_book = customtkinter.CTkImage(light_image=Image.open("return_book.png"),size=(250,300))

#=======================================================================================================================
#=======================================================================================================================
# Sign_Up window formatting
def sign_up():
        
    def submit(a):
         
        def destroy():
            success_win.destroy()
            signup_win.destroy()
            
        if pass1.get() != pass2.get():
           error = customtkinter.CTkToplevel(signup_win)
           error.resizable(False,False)
           error.title("Error occured")
           customtkinter.CTkLabel(error,image=warning_image,text="").place(x=20,y=27)
           customtkinter.CTkLabel(error,text="Both passwords\nmust be same",font=("Consolas",16)).pack(side="top",pady=27,padx=70)
           customtkinter.CTkButton(error,text="OK",fg_color="#2b52ff",width=100,command=lambda:error.destroy()).pack(side="top",pady=(0,20))
        if pass1.get() == pass2.get():
            try:
                file = open('User_pass.txt','r+')
                d = file.read()
                f = ast.literal_eval(d)
                user_password = { newuser.get() : pass1.get() }
                f.update(user_password)
                file.close()
                file = open('User_pass.txt','w')
                w = file.write(str(f))
                
            except:
                file = open('User_pass.txt','w')
                f = str({newuser.get():pass1.get()})
                file.write(f)
                file.close()
            success_win = customtkinter.CTkToplevel(signup_win)
            success_win.title("Successfully Registered")
            success_win.wm_iconbitmap("icon.ico")
            success_win.geometry("250x125")
            success_win.resizable(False,False)
            frame = customtkinter.CTkFrame(success_win)
            frame.pack(padx=10,pady=10,fill="both",expand="true")
            customtkinter.CTkLabel(frame,text="Sign up\nSuccessfull!",font=("Consolas",16)).pack(side="top",padx=(40,30),pady=(20,12))
            customtkinter.CTkLabel(frame,text="",image=success_image).place(x=23,y=27)
            customtkinter.CTkButton(frame,text="Ok",width=100,fg_color="#2b52ff",font=("Consolas",19,"bold"),command=destroy).pack(side="top",padx=70)
            
    def enter_user(event):
        newuser.configure(width=270)
        newuser.place(x=540)

    def leave_user(event):
        newuser.configure(width=250)
        newuser.place(x=550)
        
    def btn_enter(event): 
        sign_in_btn.configure(width=140,height=40)
        sign_in_btn.place(x=610,y=245)

    def btn_leave(event):
        sign_in_btn.configure(width=120,height=30)
        sign_in_btn.place(x=620,y=250)
        
    def user_enter(e):
        name = newuser.get()
        if name == "" or name == "Username":
            newuser.delete(0,END)

    def user_leave(e):
        name = newuser.get()
        if name == '':
            newuser.insert(0,"Username")

    def pass1_enter(e):
        name = pass1.get()
        if name == "" or name == "Password":
            pass1.delete(0,END)
            pass1.configure(show="*")

    def pass1_leave(e):
        name = pass1.get()
        if name == '':
            pass1.insert(0,"Password") 
            pass1.configure(show="")  
        
    def enter_pass1(event):
        pass1.configure(width=270)
        pass1.place(x=540)

    def leave_pass1(event):
        pass1.configure(width=250)
        pass1.place(x=550)
        
    def enter_pass2(event):
        pass2.configure(width=270)
        pass2.place(x=540)

    def leave_pass2(event):
        pass2.configure(width=250)
        pass2.place(x=550)
        
    def pass2_enter(e):
        name = pass2.get()
        if name == "" or name == "Confirm Password":
            pass2.delete(0,END)
            pass2.configure(show="*")

    def pass2_leave(e):
        name = pass2.get()
        if name == '':
            pass2.insert(0,"Confirm Password")
            pass2.configure(show="")
            
    def btn_enter(event):
        sign_up_btn.configure(width=140,height=40)
        sign_up_btn.place(x=610,y=260)

    def btn_leave(event):
        sign_up_btn.configure(width=120,height=30)
        sign_up_btn.place(x=620,y=265)
    
    signup_win = customtkinter.CTkToplevel(window)
    signup_win.title("Sign Up")
    signup_win.geometry("880x450+100+150")
    signup_win.wm_iconbitmap("icon.ico")
    signup_win.resizable(False,False)
    signup_win.bind('<Return>',submit)
    
    img_lbl = customtkinter.CTkLabel(signup_win,image=signup_image,text="")
    img_lbl.pack(side="left")
    label = customtkinter.CTkLabel(signup_win,text="Signup Now",font=("seoge UI",24,"bold"))
    label.place(x=600,y=70)
    newuser = customtkinter.CTkEntry(signup_win,height=35,width=250,justify="center",border_color="#fff",border_width=0,font=("Cascadia",16))
    newuser.place(x=550,y=115)
    newuser.insert(0,"Username")
    newuser.bind('<FocusIn>',user_enter)
    newuser.bind('<FocusOut>',user_leave)
    newuser.bind('<Enter>',enter_user)
    newuser.bind('<Leave>',leave_user)
    
    pass1 = customtkinter.CTkEntry(signup_win,height=35,width=250,justify="center",border_width=0,border_color="#fff",font=("Cascadia",18))
    pass1.place(x=550,y=165)
    pass1.insert(0,"Password")
    pass1.bind('<FocusIn>',pass1_enter)
    pass1.bind('<FocusOut>',pass1_leave)
    pass1.bind('<Enter>',enter_pass1)
    pass1.bind('<Leave>',leave_pass1)
    
    pass2 = customtkinter.CTkEntry(signup_win,height=35,width=250,justify="center",border_width=0,border_color="#fff",font=("Cascadia",18))
    pass2.place(x=550,y=215)
    pass2.insert(0,"Confirm Password")
    pass2.bind('<FocusIn>',pass2_enter)
    pass2.bind('<FocusOut>',pass2_leave)
    pass2.bind('<Enter>',enter_pass2)
    pass2.bind('<Leave>',leave_pass2)
    
    sign_up_btn = customtkinter.CTkButton(signup_win,text="Submit",height=30,fg_color="#2b52ff",width=120,corner_radius=10,text_color="#fff",command=lambda:submit(0))
    sign_up_btn.place(x=620,y=265)
    sign_up_btn.bind('<Enter>',btn_enter)
    sign_up_btn.bind('<Leave>',btn_leave)
    
    sign_in_btn = customtkinter.CTkButton(signup_win,text="Sign In",fg_color="transparent",hover_color="",text_color="#2b52ff",command=lambda:signup_win.destroy())
    sign_in_btn.place(x=675,y=305)
    sign_in_label = customtkinter.CTkLabel(signup_win,text="I already have an account!")
    sign_in_label.place(x=575,y=305)

#=================================================================================================================
#=================================================================================================================
#formatting the library_page page

def update_page(val,str1):
    val.configure(state="normal")
    val.delete("0.0",END)
    val.insert(END,str1)
    val.configure(state="disabled")
    f = open("ledger.txt","a")
    f.write(str1)
    f.close()

def library_page(str):
    
    def fill_textboxes(string):
        avail_book_textbox.configure(state="normal")
        file = open(f'{string}','r')
        f = file.read()
        avail_book_textbox.insert(END,f)
        avail_book_textbox.configure(state="disabled")
    
    def Add():
        count =0
        value = user_entry_textbox.get("0.0","end")
        f = open('Books.txt','r+')
        for book_name in f:
            if value == book_name:
                update_page(update_textbox,"Book is already\npresent in the libarary!")
                f.close()
                count = 1
                break
        if count == 0:
            f = open('Books.txt','a')
            f.write(value)
            f.close()
            update_page(update_textbox,f"Book <{value}> has been added in the\nLibrary by the user {username.get()} ")
            fill_textboxes('Books.txt')
    
    def Issue():
        issue_count = 0
        value = user_entry_textbox.get("0.0","end")
        f = open('Books.txt','r+')
        for book_name in f:
            if value == book_name:
                update_page(update_textbox,f"Book <{value}> has been issued to user {username.get()}")
                issue_count = 1
                print(value)
        f.close()
        if issue_count == 1:
            try:
                with open('Books.txt', 'r') as fr:
                    lines = fr.readlines()
 
                with open('temp.txt', 'w') as fw:
                    for line in lines:
                        if line.strip('\n') != value:
                                fw.write(line)
                                print("Deleted")
            except:
                 print("Oops! something error")
        fill_textboxes('temp.txt')
        f.close()
        if issue_count == 0:
            update_page(update_textbox,f"Book <{value}> is not present in the library!")
                   
    def Return():
        count =0
        value = user_entry_textbox.get("0.0","end")
        f = open('Books.txt','r+')
        for book_name in f:
            if value == book_name:
                update_page(update_textbox,"Book is already\npresent in the libarary!")
                f.close()
                count = 1
                break
        if count == 0:
            f = open('Books.txt','a')
            f.write(value)
            f.close()
            update_page(update_textbox,f"Book <{value}> has been returned in the\nLibrary by the user {username.get()} ")
            fill_textboxes('Books.txt')
                
    library = customtkinter.CTkToplevel()
    library.title(f"{str} Book")
    library.geometry("880x500")
    library.wm_iconbitmap("icon.ico")
    library.resizable(False,False)
    left_frame = customtkinter.CTkFrame(library,width=300)
    left_frame.pack(side="left",padx=10,pady=10,fill="y",expand="true")
    right_frame = customtkinter.CTkFrame(library,width=550)
    right_frame.pack(side="left",padx=(0,10),pady=10,fill="y",expand="true")
    customtkinter.CTkLabel(left_frame,text="Please Enter\nthe Book name",font=("seoge UI",28,"bold")).place(x=45,y=55)
    user_entry_textbox =customtkinter.CTkTextbox(left_frame,height=200,width=280,font=("seoge UI",16))
    user_entry_textbox.place(x=10,y=140)
    customtkinter.CTkLabel(right_frame,text="Available Books\nin the library are",font=("seoge UI",28,"bold")).place(x=25,y=62)
    update_textbox = customtkinter.CTkTextbox(right_frame,width=250,height=100,font=("seoge UI",16))
    update_textbox.place(x=290,y=30)
    update_textbox.configure(state="disabled")
    avail_book_textbox = customtkinter.CTkTextbox(right_frame,width=530,height=330,font=("seoge UI",16))
    avail_book_textbox.place(x=10,y=140)

    fill_textboxes("Books.txt")
    if str == 'Add':
        customtkinter.CTkButton(left_frame,text=f"{str} Now",width=150,height=50,fg_color="#2b52ff",font=("seoge UI",20,"bold"),command=Add).place(x=75,y=360)
    if str == 'Issue':
        customtkinter.CTkButton(left_frame,text=f"{str} Now",width=150,height=50,fg_color="#2b52ff",font=("seoge UI",20,"bold"),command=Issue).place(x=75,y=360)
    if str == 'Return':
        customtkinter.CTkButton(left_frame,text=f"{str} Now",width=150,height=50,fg_color="#2b52ff",font=("seoge UI",20,"bold"),command=Return).place(x=75,y=360)

#=================================================================================================================
#=================================================================================================================
# choosing the book modes
def new_window():
    new_win = customtkinter.CTkToplevel(window)
    new_win.title("Choose your option")
    new_win.wm_iconbitmap("icon.ico")
    new_win.geometry("880x500+200+100")
    new_win.resizable(False,False)
    mainframe = customtkinter.CTkFrame(new_win)
    mainframe.pack(padx=10,pady=10,fill="both",expand="true")
    frame1 = customtkinter.CTkFrame(mainframe,width=250)
    frame1.pack(padx=5,pady=10,side="left",fill="y",expand="true")
    frame2 = customtkinter.CTkFrame(mainframe,width=270)
    frame2.pack(pady=10,side="left",fill="y",expand="true")
    frame3 = customtkinter.CTkFrame(mainframe,width=250)
    frame3.pack(padx=5,pady=10,side="left",fill="y",expand="true")
    
    photo1 = customtkinter.CTkLabel(frame1,text="",image=add_book)
    photo1.place(x=0,y=160)
    photo2 = customtkinter.CTkLabel(frame2,text="",image=issue_book)
    photo2.place(x=0,y=180)
    photo3 = customtkinter.CTkLabel(frame3,text="",image=return_book)
    photo3.place(x=0,y=180)
    
    customtkinter.CTkButton(frame1,text="Add Book",width=180,height=70,fg_color="#2b52ff",font=("seoge UI",24,"bold"),command=lambda:library_page("Add")).place(x=30,y=80)
    customtkinter.CTkButton(frame2,text="Issue Book",width=180,height=70,fg_color="#2b52ff",font=("seoge UI",24,"bold"),command=lambda:library_page("Issue")).place(x=40,y=80)
    customtkinter.CTkButton(frame3,text="Return Book",width=180,height=70,fg_color="#2b52ff",font=("seoge UI",24,"bold"),command=lambda:library_page("Return")).place(x=40,y=80)
    
#=================================================================================================================
#=================================================================================================================
# formatting the sign in page
i= 0
def change_mode():
    global i
    if i== 0:
        customtkinter.set_appearance_mode("dark")
        mode_btn.configure(image=dark_mode)
        i = i+1
    elif i == 1:
        customtkinter.set_appearance_mode("light")
        mode_btn.configure(image=light_mode)
        i = i-1

def sign_in(a):
    
    def destroy_now():
        signin_success.destroy()
        new_window()
    
    count = 0
    f = open("User_pass.txt","rt")
    line = f.read()
    r = ast.literal_eval(line)
    for k,v in r.items():
        if username.get() == k and password.get() == v:
            count = 1
            signin_success = customtkinter.CTkToplevel(window)
            signin_success.geometry("300x150+500+250")
            signin_success.title("Successful")
            signin_success.wm_iconbitmap("icon.ico")
            frame = customtkinter.CTkFrame(signin_success)
            frame.pack(fill="both",expand="true",padx=10,pady=15)
            label = customtkinter.CTkLabel(frame,image=success_image,text="")
            label.place(x=50,y=27)
            label = customtkinter.CTkLabel(frame,text="Sign in\nSuccessful!",font=("Consolas",16))
            label.pack(side="top",pady=25)
            customtkinter.CTkButton(frame,text="OK",fg_color="#2b52ff",command=destroy_now).pack(side="top")
        
    if count == 0:
            error = customtkinter.CTkToplevel(window)
            error.geometry("300x150+500+250")
            error.title("Error")
            error.wm_iconbitmap("icon.ico")
            frame = customtkinter.CTkFrame(error)
            frame.pack(fill="both",expand="true",padx=10,pady=15)
            label = customtkinter.CTkLabel(frame,image=warning_image,text="")
            label.place(x=20,y=27)
            label = customtkinter.CTkLabel(frame,text="Please enter your\nvalid credentials",font=("Consolas",16))
            label.pack(side="top",pady=25)
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
    
def btn_enter(event):
    sign_in_btn.configure(width=140,height=40)
    sign_in_btn.place(x=610,y=245)

def btn_leave(event):
    sign_in_btn.configure(width=120,height=30)
    sign_in_btn.place(x=620,y=250)
    
def user_enter(e):
    name = username.get()
    if name == "" or name == "Username":
        username.delete(0,END)

def user_leave(e):
    name = username.get()
    if name == '':
        username.insert(0,"Username")

def pass_enter(e):
    name = password.get()
    if name == "" or name == "Password":
        password.delete(0,END)
        password.configure(show="*")

def pass_leave(e):
    name = password.get()
    if name == '': 
        password.insert(0,"Password")
        password.configure(show="")
    
window = customtkinter.CTk() 
window.geometry("880x500+400+120")
window.title("library Management By Mohit kumar")
window.wm_iconbitmap("icon.ico")
window.resizable(False,False)
window.bind('<Return>',sign_in)

image_label = customtkinter.CTkLabel(window,image=login_image,text="")
image_label.pack(side="left")
textlabel = customtkinter.CTkLabel(window,text="Welcome to the\nCity library",font=("seoge UI",24,"bold"))
textlabel.place(x=580,y=70)

mode_btn = customtkinter.CTkButton(window,height=60,text="",fg_color="transparent",hover_color="",width=60,image=light_mode,command=change_mode)
mode_btn.place(x=790,y=10)

username = customtkinter.CTkEntry(window,height=35,width=250,justify="center",border_color="#fff",border_width=0,font=("Cascadia",18))
username.place(x=550,y=150)
username.insert(0,"Username")
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

sign_in_btn = customtkinter.CTkButton(window,text="Sign in",height=30,fg_color="#2b52ff",width=120,corner_radius=10,text_color="#fff",command=lambda:sign_in(0))
sign_in_btn.place(x=620,y=250)
sign_in_btn.bind('<Enter>',btn_enter)
sign_in_btn.bind('<Leave>',btn_leave)

signup_btn = customtkinter.CTkButton(window,text="Sign Up",fg_color="transparent",hover_color="",text_color="#2b52ff",command=sign_up)
signup_btn.place(x=660,y=305)
signup_label = customtkinter.CTkLabel(window,text="Don't have an account?")
signup_label.place(x=570,y=305)
#=================================================================================================================
#=================================================================================================================
window.mainloop()
