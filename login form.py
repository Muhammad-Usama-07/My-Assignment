from tkinter import *
import Menu_page
r = Tk()

#Creating format
r.title( 'Module' )  # title
r.configure( bg = '#bcdebb' )
r.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left))
r.minsize( 400 , 200 )
r.maxsize( 1100 , 700 )
r.iconbitmap(r'model_icon.ico')
Label(r,text=" Note: Here you can make your module perfect... :) ", bg = "#66bd6d",relief = "solid",
      anchor = "w",height = 2,font="Times%New%Roman 11 bold italic").pack(side = TOP, fill = X)

# Action

def  up_to_next():
    if(User_name.get() == "Usama" and passd.get() == "raj"):
        print("its working... ")
    else:
        print("Not working")

#Creating Frame

lf1 = LabelFrame(r, text = "Login Your Account", fg = "red",bg = '#33ff9e',
                        relief = "solid",font = "Times%New%Roman 16 bold",height = 550)
lf1.pack( fill = "both",expand = TRUE,padx = 20, pady = 20 )

#Creating Label

lbl = Label(lf1, text = "User Name:",bg = '#33ff9e', font = ("Times%New%Roman",15 ,"italic", "bold"))
lbl.place(x = 100,y = 110)

User_name = StringVar()
Login_Name = Entry(lf1, textvariable = User_name, width = 25,relief = "solid", font = ("Times%New%Roman",15,"bold"))
Login_Name.place(x = 220, y = 110)

lbl = Label(lf1, text = "Password:",bg = '#33ff9e', font = ("Times%New%Roman",15,"italic" ,"bold"))
lbl.place(x = 100,y = 190)
passd = StringVar()
enter_passd = Entry(lf1, textvariable = passd, width = 25,relief = "solid", font = ("Times%New%Roman",15 ,"bold"))
enter_passd.place(x = 220, y = 190)

# Login Button
login_Button = Button(lf1, text = "Submit",bg ='#4dff4d', font = ("Times%New%Roman",15,"bold"), relief = "groove", command = up_to_next )
login_Button.place(x = 150, y = 270)






r.mainloop()
