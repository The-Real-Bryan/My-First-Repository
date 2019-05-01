import tkinter

from tkinter import scrolledtext

rob = tkinter.Tk()
rob.columnconfigure(0, minsize=100)
rob.title("Sycamail Registration Page")

#Definitions

def Homepaging():
    Homepage.tkraise()

def Pageone():
    pageOne.tkraise()

def Pagetwo():
    pageTwo.tkraise()

def Pagethree():
    pageThree.tkraise()

#Images

Sycamore = tkinter.PhotoImage(file = "Sycamore.png")
im1a = Sycamore.subsample(1)

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

#Labels

Title = tkinter.Label(Homepage, text = "Sycamail Registration", font = "Times_New_Roman, 100")
Title.configure(bg = "light green")
Title.place(relx = 0.5, rely = 0, anchor = "n")

Sycamore = tkinter.Label(Homepage, image = im1a, bg = "light green", width = 600, height = 600)
Sycamore.place(relx = 0.5, rely = 0.5, anchor = "center")

Email = tkinter.Label(pageOne, text = "E-Mail Name:", font = "Papyrus, 40")
Email.configure(bg = "light green")
Email.place(relx = 0, rely = 0)

User = tkinter.Label(pageOne, text = "Username:", font = "Papyrus, 40")
User.configure(bg = "light green")
User.place(relx = 0, rely = 0.15)

Password = tkinter.Label(pageOne, text = "Password:", font = "Papyrus, 40")
Password.configure(bg = "light green")
Password.place(relx = 0, rely = 0.3)

Name = tkinter.Label(pageOne, text = "Name:", font = "Papyrus, 40")
Name.configure(bg = "light green")
Name.place(relx = 0, rely = 0.45)

#Entries

Emailent = tkinter.Entry(pageOne, width = 60)
Emailent.place(relx = 0.2, rely = 0.016)

Userent = tkinter.Entry(pageOne, width = 60)
Userent.place(relx = 0.2, rely = 0.168)

Passwordent = tkinter.Entry(pageOne, width = 60)
Passwordent.place(relx = 0.2, rely = 0.318)

Nameent = tkinter.Entry(pageOne, width = 60)
Nameent.place(relx = 0.2, rely = 0.4685)

#Buttons

Ontopageone = tkinter.Button(Homepage, text = "Begin the Registration Now!", font = "Papyrus, 50", command = Pageone)
Ontopageone.place(relx = 0.5, rely = 0.25, anchor = "s")

Next = tkinter.Button(pageOne, text = "Ready for the Final Step!", font = "Papyrus, 35", command = Pagetwo)
Next.place(relx = 0.71, rely = 0.7)

Finished = tkinter.Button(pageTwo, text = "Proceed!", font = "Papyrus, 35", command = Pagethree)
Finished.place(relx = 0.89, rely = 0.695, anchor = "center")


#Scrolled Text Boxes


TS = scrolledtext.ScrolledText(pageTwo, width = 97, height = 10)

TS.insert(tkinter.INSERT, "You must follow any policies made available to you within the Services. Don’t misuse our Services. For example, don’t interfere with our Services or try to access them using a method other than the interface and the instructions that we provide. You may use our Services only as permitted by law, including applicable export and re-export control laws and regulations. We may suspend or stop providing our Services to you if you do not comply with our terms or policies or if we are investigating suspected misconduct. Using our Services does not give you ownership of any intellectual property rights in our Services or the content you access. You may not use content from our Services unless you obtain permission from its owner or are otherwise permitted by law. These terms do not grant you the right to use any branding or logos used in our Services. Don’t remove, obscure, or alter any legal notices displayed in or along with our Services. Our Services display some content that is not Google’s. This content is the sole responsibility of the entity that makes it available. We may review content to determine whether it is illegal or violates our policies, and we may remove or refuse to display content that we reasonably believe violates our policies or the law. But that does not necessarily mean that we review content, so please don’t assume that we do. In connection with your use of the Services, we may send you service announcements, administrative messages, and other information. You may opt out of some of those communications. Some of our Services are available on mobile devices. Do not use such Services in a way that distracts you and prevents you from obeying traffic or safety laws. Terms and Services: This is a bunch of generic, everyday 'Terms and Services' stuff that you must agree upon in order for your account to be created, please click the 'Accept' checkbox to finish creating your own E-Mail!")

TS.configure(wrap = tkinter.WORD)
TS.place(relx = 0.5, rely = 0.3, anchor = "center")

#Warning Messages




#working on it

tree = tkinter.PhotoImage(file = "tree.png")
trees = tree.subsample(1)
tree = tkinter.Label(pageOne, image = trees, bg= "light green", width = 1200, height = 1200)
tree.place(relx = 0.8, rely = 0.2, anchor = "center")

Cong = tkinter.PhotoImage(file = "Cong.png")
pizza = Cong.subsample(1)

Cong = tkinter.Label(pageThree, image = pizza, bg = "light green", width = 1200, height = 1200)
Cong.place(relx = 0.5, rely = 0.5, anchor = "center")


OntopageThree = tkinter.Button(pageThree, text = "Finish", font = "Papyrus, 50", command = Homepaging)
OntopageThree.place(relx = 0.5, rely = 0.25, anchor = "center")

rob.mainloop()
