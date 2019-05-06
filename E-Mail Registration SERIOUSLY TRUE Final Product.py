import tkinter

from tkinter import scrolledtext

from tkinter import messagebox

rob = tkinter.Tk()
rob.columnconfigure(0, minsize=100)
rob.title("Sycamail Registration Page")

#Definitions

def Homepaging():
    Homepage.tkraise()
    Emailent.delete(first = 0, last = "end")
    Userent.delete(first = 0, last = "end")
    Passwordent.delete(first = 0, last = "end")
    Nameent.delete(first = 0, last = "end")
    chk1_state.set(False)
    chk2_state.set(False)
    
def Pageone():
    pageOne.tkraise()

def Pagetwo():
  if((Emailent.get() == "") or (Userent.get() == "") or (Passwordent.get() == "") or (Nameent.get() == "")):
    messagebox.showinfo("Error!", "You have entered an invalid input(s)! To continue, fill in all of the four entry boxes!")
    print("You have entered an invalid input(s)! To continue, fill in all of the four entry boxes!")
  else:
    Yourmail.configure(text = Emailent.get() + "@sycamail.com")
    Youruser.configure(text = Userent.get())
    Namescreen.configure(text = Nameent.get() + "!")
    pageTwo.tkraise()
    print("Your E-mail input is:", Emailent.get() + "@sycamail.com")
    print("Your Username input is:", Userent.get())
    print("Your Name input is:", Nameent.get())
    print("Your Password input is:", Passwordent.get())

def reset():
    pageOne.tkraise()
    Emailent.delete(first = 0, last = "end")
    Userent.delete(first = 0, last = "end")
    Passwordent.delete(first = 0, last = "end")
    Nameent.delete(first = 0, last = "end")
    chk1_state.set(False)
    chk2_state.set(False)
    print("Entries from the last page are reset! Try not to mess up again! ;)")

def Pagethree():
   if((chk1_state.get() == True) and (chk2_state.get() == False)):
     pageThree.tkraise()
   else:
     messagebox.showinfo("Error!", "You have entered an invalid input! To finish the registration, please agree to the Terms and Conditions!")
     print("Error!", "You have entered an invalid input! To finish the registration, please agree to the Terms and Conditions!")
     chk1_state.set(False)
     chk2_state.set(False)
     
#Frames and Screens

Homepage = tkinter.Frame(rob, bg = "light green", height = 1400, width = 2000)
Homepage.grid_propagate(False)
Homepage.grid(row = 0, column = 0, sticky = "nsew")
pageOne = tkinter.Frame(rob, bg = "light green")
pageOne.grid(row = 0, column = 0, sticky = "nsew")
pageTwo = tkinter.Frame(rob, bg = "light green")
pageTwo.grid(row = 0, column = 0, sticky = "nsew")
pageThree = tkinter.Frame(rob, bg = "light green")
pageThree.grid(row = 0, column = 0, sticky = "nsew")

Homepage.tkraise()

#Images

Sycamore = tkinter.PhotoImage(file = "Sycamore.png")
im1a = Sycamore.subsample(1)

tree = tkinter.PhotoImage(file = "tree.png")
trees = tree.subsample(1)

Cong = tkinter.PhotoImage(file = "Cong.png")
pizza = Cong.subsample(3)

#Entries

Emailent = tkinter.Entry(pageOne, width = 60)
Emailent.place(relx = 0.15, rely = 0.0125)

Userent = tkinter.Entry(pageOne, width = 60)
Userent.place(relx = 0.15, rely = 0.1625)

Nameent = tkinter.Entry(pageOne, width = 60)
Nameent.place(relx = 0.15, rely = 0.3125)

Passwordent = tkinter.Entry(pageOne, show = "*", width = 60)
Passwordent.place(relx = 0.15, rely = 0.4625)

#Labels

Title = tkinter.Label(Homepage, text = "Sycamail Registration", font = "Papyrus, 100")
Title.configure(bg = "light green")
Title.place(relx = 0.35, rely = 0, anchor = "n")

Sycamore = tkinter.Label(Homepage, image = im1a, bg = "light green", width = 600, height = 600)
Sycamore.place(relx = 0.35, rely = 0.40, anchor = "center")

Note = tkinter.Label(pageOne, text = "NOTE: @sycamail.com will be automatically placed!", bg = "light green", fg = "red", font = "Papyrus, 20")
Note.place(relx = 0.45, rely = 0.011)

Email = tkinter.Label(pageOne, text = "E-Mail Name:", font = "Papyrus, 40")
Email.configure(bg = "light green", fg = "blue")
Email.place(relx = 0, rely = 0)

User = tkinter.Label(pageOne, text = "Username:", font = "Papyrus, 40")
User.configure(bg = "light green", fg = "yellow")
User.place(relx = 0, rely = 0.15)

Name = tkinter.Label(pageOne, text = "Name:", font = "Papyrus, 40")
Name.configure(bg = "light green", fg = "orange")
Name.place(relx = 0, rely = 0.3)

Password = tkinter.Label(pageOne, text = "Password:", font = "Papyrus, 40")
Password.configure(bg = "light green", fg = "red")
Password.place(relx = 0, rely = 0.45)

tree = tkinter.Label(pageOne, image = trees, bg = "light green", width = 450, height = 450)
tree.place(relx = 0.625, rely = 0.33, anchor = "center")

Terms = tkinter.Label(pageTwo, text = "Terms and Services:", bg = "light green", font = "Papyrus, 40")
Terms.place(relx = 0.365, rely = 0, anchor = "n")

Cong = tkinter.Label(pageThree, image = pizza, bg = "light green", width = 400, height = 230)
Cong.place(relx = 0, rely = 0)

Namescreen = tkinter.Label(pageThree, text = " ", bg = "light green", fg = "orange", font = "Papyrus, 40")
Namescreen.place(relx = 0.25, rely = 0)

UMessage = tkinter.Label(pageThree, text = "Your Username is:", bg = "light green", fg = "yellow", font = "Papyrus, 40")
UMessage.place(relx = 0.25, rely = 0.1)

Youruser = tkinter.Label(pageThree, text = " ", bg = "light green", fg = "yellow", font = "Papyrus, 40")
Youruser.place(relx = 0.25, rely = 0.15)

EMessage = tkinter.Label(pageThree, text = "Your brand new E-mail is:", bg = "light green", fg = "blue", font = "Papyrus, 40")
EMessage.place(relx = 0.25, rely = 0.3)

Yourmail = tkinter.Label(pageThree, text = " ", bg = "light green", fg = "blue", font = "Papyrus, 40")
Yourmail.place(relx = 0.22, rely = 0.35)

Enjoy = tkinter.Label(pageThree, text = "Enjoy your brand new Sycamail Account!", bg = "light green", font = "Papyrus, 40")
Enjoy.place(relx = 0.2, rely = 0.525)

#Buttons

Ontopageone = tkinter.Button(Homepage, text = "Begin the Registration Now!", fg = "green", font = "Papyrus, 50", command = Pageone)
Ontopageone.place(relx = 0.35, rely = 0.20, anchor = "s")

Next = tkinter.Button(pageOne, text = "Ready for the Final Step!", fg = "green", font = "Papyrus, 35", command = Pagetwo)
Next.place(relx = 0.5125, rely = 0.54)

Finished = tkinter.Button(pageTwo, text = "Proceed!", fg = "green", font = "Papyrus, 35", command = Pagethree)
Finished.place(relx = 0.6815, rely = 0.5575, anchor = "center")

Reset = tkinter.Button(pageTwo, text = "Reset!", fg = "green", font = "Papyrus, 35", command = reset)
Reset.place(relx = 0.6, rely = 0.5575, anchor = "center")

Ontohomepage = tkinter.Button(pageThree, text = "Finished!", fg = "green", font = "Papyrus, 50", command = Homepaging)
Ontohomepage.place(relx = 0.61, rely = 0.525)

#Scrolled Text Boxes

TS = scrolledtext.ScrolledText(pageTwo, width = 97, height = 10)

TS.insert(tkinter.INSERT, "You must follow any policies made available to you within the Services. Don’t misuse our Services. For example, don’t interfere with our Services or try to access them using a method other than the interface and the instructions that we provide. You may use our Services only as permitted by law, including applicable export and re-export control laws and regulations. We may suspend or stop providing our Services to you if you do not comply with our terms or policies or if we are investigating suspected misconduct. Using our Services does not give you ownership of any intellectual property rights in our Services or the content you access. You may not use content from our Services unless you obtain permission from its owner or are otherwise permitted by law. These terms do not grant you the right to use any branding or logos used in our Services. Don’t remove, obscure, or alter any legal notices displayed in or along with our Services. Our Services display some content that is not Google’s. This content is the sole responsibility of the entity that makes it available. We may review content to determine whether it is illegal or violates our policies, and we may remove or refuse to display content that we reasonably believe violates our policies or the law. But that does not necessarily mean that we review content, so please don’t assume that we do. In connection with your use of the Services, we may send you service announcements, administrative messages, and other information. You may opt out of some of those communications. Some of our Services are available on mobile devices. Do not use such Services in a way that distracts you and prevents you from obeying traffic or safety laws. Terms and Services: This is a bunch of generic, everyday 'Terms and Services' stuff that you must agree upon in order for your account to be created, please click the 'Accept' checkbox to finish creating your own E-Mail!")
TS.configure(wrap = tkinter.WORD)
TS.configure(state = "disabled")
TS.place(relx = 0.375, rely = 0.2, anchor = "center")

#Checkboxes

chk1_state = tkinter.BooleanVar()
chk1_state.set(False)
check1 = tkinter.Checkbutton(pageTwo, bg = "light green", var = chk1_state, text = "Agree", fg = "blue", font = "Papyrus, 30", onvalue = 1, offvalue = 0)
check1.place(relx = 0.24, rely = 0.4)

chk2_state = tkinter.BooleanVar()
chk2_state.set(False)
check2 = tkinter.Checkbutton(pageTwo, bg = "light green", var = chk2_state, text = "Disagree", fg = "red", font = "Papyrus, 30", onvalue = 1, offvalue = 0)
check2.place(relx = 0.44, rely = 0.4)

#End of Program

rob.mainloop()
