from tkinter import *


class Menu_class():
    def menu_window():
        menu_window_var = Toplevel()
        menu_window_var.title( 'Menu Window' )
        menu_window_var.geometry("900x600+300+50")
        menu_window_var.minsize(400, 200)
        menu_window_var.maxsize(1100, 700)
        menu_window_var.configure(bg='#bcdebb')
        Label(menu_window_var, text=" Note: Here you can make your module perfect... :) ", bg="#66bd6d", relief="solid",
              anchor="w", height=2, font="Times%New%Roman 11 bold italic").pack(side=TOP, fill=X)

        lf = LabelFrame(menu_window_var, text="Enter Your choice", fg="red", bg='#33ff9e',
                         relief="solid", font="Times%New%Roman 16 bold", height=550)
        lf.pack(fill="both", expand=TRUE, padx=20, pady=20)
        next_button = Button(lf, text="Next", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"), relief="groove")
        next_button.place(x=750, y=430)

        #Back_Button = Button(lf, text="Back", bg='#4dff4d', font=("Times%New%Roman", 15, "bold"), relief="groove", command = menu_window_var.destroy)
        #Back_Button.place(x=650, y=430)

    def Mennu():
        r = Tk()
        #Creating format
        r.title( 'Module' )  # title
        r.configure( bg = '#bcdebb' )
        r.geometry( "900x600+300+50" )  # (width X hight + from_right + from_left))
        r.minsize( 400 , 200 )
        r.maxsize( 1100 , 700 )
        Label(r,text=" Note: Here you can make your module perfect... :) ", bg = "#66bd6d",relief = "solid",
              anchor = "w",height = 2,font="Times%New%Roman 11 bold italic").pack(side = TOP, fill = X)

        # Action

        def  up_to_next():
            if(User_name.get() == "Usama" and passd.get() == "raj"):
                print("its working... ")
            else:
                print("Not working")

        #Creating Frame

        lf1 = LabelFrame(r, text = "Enter Your choice", fg = "red",bg = '#33ff9e',
                                relief = "solid",font = "Times%New%Roman 16 bold",height = 550)
        lf1.pack( fill = "both",expand = TRUE,padx = 20, pady = 20 )

        #Creating Label



        # Login Button
        next_button = Button(lf1, text = "Next",bg ='#4dff4d', font = ("Times%New%Roman",15,"bold"), relief = "groove", command = menu_window )
        next_button.place(x = 750, y = 430)

        Back_Button = Button(lf1, text = "Back",bg ='#4dff4d', font = ("Times%New%Roman",15,"bold"), relief = "groove" )
        Back_Button.place(x = 650, y = 430)




        r.mainloop()
