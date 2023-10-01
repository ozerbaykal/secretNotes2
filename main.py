from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox





#Screen
window=Tk()
window.minsize(width="400",height="650")
window.title("My Secret Notes")
window.config(background="light blue")

import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)







def decrpyt():
    massage_decrypt=My_secret_text.get("1.0",END)
    password=masterkey_entry.get()

    if len(massage_decrypt)==0 or len(password)==0 :
        messagebox.showerror("error","ENTER YOUR VALİD İNPUT")

        




    else:
       try:
            decrpyted_message=decode(password,massage_decrypt)
            My_secret_text.delete("1.0",END)
            My_secret_text.insert("1.0",decrpyted_message)
       except:
           messagebox.showerror("error","please enter correct info" )

def save_title():

    Note1=entry_title.get()
    secret=My_secret_text.get("1.0",END)
    password= masterkey_entry.get()


    if not Note1 :
        messagebox.showerror("error", "enter your file name ")
    elif not secret:
        messagebox.showerror("error", "enter your secret ")

    elif not password :
        messagebox.showerror("error", "enter your password")
    else:
        message_encrypt=encode(password,secret)
        try:
         with open("mysecret.txt","a")as file:
             file.write(f" \n{Note1}\n{message_encrypt}")

        except FileNotFoundError:
            with open("mysecret.txt","w") as file:
                file.write(f" \n{Note1}\n{message_encrypt}")
        finally:
            entry_title.delete(0,END)
            My_secret_text.delete("1.0",END)
            masterkey_entry.delete(0,END)



        file.close()
        messagebox.showerror("Done", "secret is updated")



entry_title=Entry(width="30")
entry_title.place(y="150",x="115")
title_note_label=Label(text="Enter your title",font=("arial",11,"bold"))
title_note_label.place(x="155",y="123")
title_note_label.config(bg="light grey",fg="black")
title_secret_label=Label(text="Enter your secret",font=("arial",11,"bold"))
title_secret_label.place(x="145",y="175")
title_secret_label.config(bg="light grey",fg="black")

My_secret_text=Text(width=35,height=17)
My_secret_text.place(x="70",y="205")
masterkey_label=Label(text="Enter master Key!!!")
masterkey_label.place(x="140",y="490")
masterkey_label.config(font=("arial",11,"bold"),bg="light grey")
masterkey_entry=Entry(width="30")
masterkey_entry.place(x="120",y="520")






save_encrypt_button=Button(text="Save & Encrypt ")

save_encrypt_button.config(command=save_title)


save_encrypt_button.place(x="165",y="545")
dcrypt_button=Button(text="Dycrypt")
dcrypt_button.place(x="180",y="585")
dcrypt_button.config(bg="dark grey")
dcrypt_button.config(command=decrpyt)
save_encrypt_button.config(bg="dark grey")


image=PhotoImage(file="secret_k.png")
image_label=Label(image=image)
image_label.place(x=160,y=20)

















window.mainloop()