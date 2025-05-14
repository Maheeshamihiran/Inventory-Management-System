from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import datetime

#---------------------------------function part--------------------------------------------------------------
def employee_form():
    global back_image  # Keep track of image reference

    employee_form = Frame(window, width=1190, height=720, bg="white")
    employee_form.place(x=280, y=100)

    employee_title_form = Label(employee_form, text="Manage Employee Details", 
                              font=("times new roman", 15, "bold"),
                              bg="#0f4d7d", fg='white')
    employee_title_form.place(x=0, y=0, relwidth=1)

    # Correct way to load the image
    back_image = PhotoImage(file="arrow-left1.png")  # Use file parameter

    # Create button with the image
    back_button = Button(employee_form, image=back_image,bg="white",bd=0,cursor='hand2',command=lambda:employee_form.place_forget())  # Use back_image instead of back_button
    back_button.place(x=0, y=30,width=80)

    Top_frame= Frame(employee_form,bg='whiteSmoke',bd=1)
    Top_frame.place(x=0,y=70,height=270,relwidth=1)

    search_frame=Frame(Top_frame,bg='white')
    search_frame.pack()

    Search_combo=ttk.Combobox(search_frame,values=('id','Name','Email'),font=('times new roman',14,'bold'),state='readonly')
    Search_combo.set('Search By')
    Search_combo.grid(row=0,column=0,padx=20)

    Search_combo_entry=Entry(search_frame,font=("times new romman",16,"bold"),bg='lightyellow')
    Search_combo_entry.grid(row=0,column=1,padx=20)

    search_button=Button(search_frame,font=("times new roman",12,'bold'),cursor='hand2',text="Search",bg="SteelBlue4")
    search_button.grid(row=0,column=2,padx=30)

    show_button=Button(search_frame,font=("times new roman",12,"bold"),cursor='hand2',text="Show All",bg="SteelBlue4")
    show_button.grid(row=0,column=3,padx=30)

    # Create scrollbars
    HORIZONTAL_scrollbar = Scrollbar(Top_frame, orient=HORIZONTAL)
    VERTICAL_scrollbar = Scrollbar(Top_frame, orient=VERTICAL)

    # Create treeview with scrollbar configuration
    employee_treeview = ttk.Treeview(
        Top_frame, 
        columns=('empid', 'name', 'email', 'gender', 'dob', 'employee_type', 
                'education', 'salary', 'address', 'workshift', 'doj', 
                'contact', 'user_type'),
        show='headings',
        yscrollcommand=VERTICAL_scrollbar.set,
        xscrollcommand=HORIZONTAL_scrollbar.set
    )

    # Configure scrollbars
    HORIZONTAL_scrollbar.pack(side=BOTTOM, fill=X)
    VERTICAL_scrollbar.pack(side=RIGHT, fill=Y)
    
    # Connect scrollbars to treeview
    HORIZONTAL_scrollbar.configure(command=employee_treeview.xview)
    VERTICAL_scrollbar.configure(command=employee_treeview.yview)

    employee_treeview.heading('empid', text='Employee ID')
    employee_treeview.heading('name', text='Name')
    employee_treeview.heading('email', text='Email')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('dob', text='Date of Birth')
    employee_treeview.heading('employee_type', text='Employee Type')
    employee_treeview.heading('education', text='Education')
    employee_treeview.heading('salary', text='Salary')
    employee_treeview.heading('address', text='Address')
    employee_treeview.heading('workshift', text='Work Shift')
    employee_treeview.heading('doj', text='Date of Joining')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('user_type', text='User Type')
    employee_treeview.column('empid', width=100)
    employee_treeview.column('name', width=150)
    employee_treeview.column('email', width=200)
    employee_treeview.column('gender', width=100)
    employee_treeview.column('dob', width=120)
    employee_treeview.column('employee_type', width=150)
    employee_treeview.column('education', width=150)
    employee_treeview.column('salary', width=120)
    employee_treeview.column('address', width=200)
    employee_treeview.column('workshift', width=120)
    employee_treeview.column('doj', width=120)
    employee_treeview.column('contact', width=150)
    employee_treeview.column('user_type', width=150)
    employee_treeview.pack(fill=BOTH, expand=True, padx=20,pady=20)


    hor
    




        

#------------------------------GUI part-----------------------------------------------------------------------

#create a window
window=Tk()
window.title("Dashboard")
window.geometry("1470x820+225+115")
window.configure(bg="White")
window.resizable(False,False)
bg_image=PhotoImage(file="inventory-system2.png")
#create a title label
titleLabel=Label(window,image=bg_image,compound=LEFT,text="      Inventory Management System",font=("times new roman",40,"bold"),bg="#010c48",fg="WhiteSmoke",anchor="w",padx=20)
titleLabel.place(x=0,y=0,relwidth=1)


Buttonlogout=Button(titleLabel,text="Logout",font=("times new roman",20,"bold"),bg="SteelBlue4",fg="white",cursor="hand2")
Buttonlogout.place(x=1270,y=10,width=170,height=50)
#create a date and time label
time_str=datetime.datetime.now().strftime("%H:%M:%S")
date_str=datetime.datetime.now().strftime("%Y-%m-%d")
timedateLabel=Label(window,text=f"Welcome Admin\t\t\tDate: {date_str}\t\t\tTime: {time_str}  ",font=("times new roman",15 ,"bold"),bg="SlateGray4",fg="WhiteSmoke")
timedateLabel.place(x=0,y=70,relwidth=1)

#creating a frame for the left side menu

left_frame=Frame(window,bd=1,relief=RIDGE,bg="white")
left_frame.place(x=0,y=100,width=280,height=710)

dashboard_title=Label(left_frame,text="Dashboard",font=("times new roman",32,"bold"),bg="steelBlue",fg="white")
dashboard_title.pack(fill=X)

logo_image=PhotoImage(file="logo1.png")
logo_label=Label(left_frame,image=logo_image,bd=0,anchor="nw",bg="white")
logo_label.pack(pady=20)

#creating a button for the left side menu


menuLable=Label(left_frame,text="Menu",font=("times new roman",25,"bold"),bg="green",fg="WhiteSmoke")
menuLable.pack(fill=X)
#employee button
employee_image=PhotoImage(file="employee1.png")


employees_button=Button(left_frame,image=employee_image,compound=LEFT,text="  Employees",font=("times new roman",20,"bold"),bg="SlateGray4",fg="WhiteSmoke",cursor="hand2",anchor="w",padx=10,command=employee_form)
employees_button.pack(fill=X)
#suppliers button
suppliers_image=PhotoImage(file="tracking1.png")

suppliers_button=Button(left_frame,image=suppliers_image,compound=LEFT,text="  Suppliers",font=("times new roman",20,"bold"),bg="SlateGray4",fg="WhiteSmoke",cursor="hand2",anchor="w",padx=10)
suppliers_button.pack(fill=X)

#categeories button
categories_image=PhotoImage(file="categorization1.png")

categories_button=Button(left_frame,image=categories_image,compound=LEFT,text="  Categories",font=("times new roman",20,"bold"),bg="SlateGray4",fg="WhiteSmoke",cursor="hand2",anchor="w",padx=10)
categories_button.pack(fill=X)

#products button
products_image=PhotoImage(file="order1.png")

products_button=Button(left_frame,image=products_image,compound=LEFT,text="  Products",font=("times new roman",20,"bold"),bg="SlateGray4",fg="WhiteSmoke",cursor="hand2",anchor="w",padx=10)
products_button.pack(fill=X)
#sales button
sales_image=PhotoImage(file="sales1.png")

sales_button=Button(left_frame,image=sales_image,compound=LEFT,text="  Sales",font=("times new roman",20,"bold"),bg="SlateGray4",fg="WhiteSmoke",cursor="hand2",anchor="w",padx=10)
sales_button.pack(fill=X, ) 
#exit button
exit_image=PhotoImage(file="logout1.png")
exit_button=Button(left_frame,image=exit_image,compound=LEFT,text="  Exit",font=("times new roman",20,"bold"),bg="SlateGray4",fg="WhiteSmoke",cursor="hand2",command=window.destroy,anchor="w",padx=10)
exit_button.pack(fill=X)



#creating a frame for employee management

total_employee_frame=Frame(window,bd=3,relief=RIDGE,bg="#2c3e50")

total_employee_frame.place(x=470,y=120,width=350,height=220)


total_employee_frame_image=PhotoImage(file="employee (1).png")
total_employee_frame_label=Label(total_employee_frame,image=total_employee_frame_image,bd=0,bg="#2c3e50")
total_employee_frame_label.pack(pady=10)
total_employee_label=Label(total_employee_frame,text=" Total Employees ",font=("times new roman",30,"bold"),bg="#2c3e50",fg="WhiteSmoke")
total_employee_label.pack()

total_employee_count_label=Label(total_employee_frame,text=" 0 ",font=("times new roman",30,"bold"),bg="#2c3e50",fg="WhiteSmoke")
total_employee_count_label.pack()

#suppliers frame

total_supplier_frame=Frame(window,bd=3,relief=RIDGE,bg="magenta4")

total_supplier_frame.place(x=900,y=120,width=350,height=220)


total_supplier_frame_image=PhotoImage(file="supplier1.png")
total_supplier_frame_label=Label(total_supplier_frame,image=total_supplier_frame_image,bd=0,bg="magenta4")
total_supplier_frame_label.pack(pady=10)
total_supplier_label=Label(total_supplier_frame,text=" Total Suppiers ",font=("times new roman",30,"bold"),bg="magenta4",fg="WhiteSmoke")
total_supplier_label.pack()

total_supplier_count_label=Label(total_supplier_frame,text=" 0 ",font=("times new roman",30,"bold"),bg="magenta4",fg="WhiteSmoke")
total_supplier_count_label.pack()

#total categories
total_categories_frame=Frame(window,bd=3,relief=RIDGE,bg="seagreen3")

total_categories_frame.place(x=470,y=360,width=350,height=220)


total_categories_frame_image=PhotoImage(file="categories.png")
total_categories_frame_label=Label(total_categories_frame,image=total_categories_frame_image,bd=0,bg="seagreen3")
total_categories_frame_label.pack(pady=10)
total_categories_label=Label(total_categories_frame,text=" Total categories ",font=("times new roman",30,"bold"),bg="seagreen3",fg="WhiteSmoke")
total_categories_label.pack()

total_categories_count_label=Label(total_categories_frame,text=" 0 ",font=("times new roman",30,"bold"),bg="seagreen3",fg="WhiteSmoke")
total_categories_count_label.pack()

#totals products

total_products_frame=Frame(window,bd=3,relief=RIDGE,bg="SteelBlue4")

total_products_frame.place(x=900,y=360,width=350,height=220)


total_products_frame_image=PhotoImage(file="total_product.png")
total_products_frame_label=Label(total_products_frame,image=total_products_frame_image,bd=0,bg="SteelBlue4")
total_products_frame_label.pack(pady=10)
total_products_label=Label(total_products_frame,text=" Total products ",font=("times new roman",30,"bold"),bg="SteelBlue4",fg="WhiteSmoke")
total_products_label.pack()
total_sales_count_label=Label(total_products_frame,text=" 0 ",font=("times new roman",30,"bold"),bg="SteelBlue4",fg="WhiteSmoke")
total_sales_count_label.pack()

#total sales



total_sales_frame=Frame(window,bd=3,relief=RIDGE,bg="#E74C3C")

total_sales_frame.place(x=685,y=600,width=350,height=220)


total_sales_frame_image=PhotoImage(file="sales.png")
total_sales_frame_label=Label(total_sales_frame,image=total_sales_frame_image,bd=0,bg="#E74C3C")
total_sales_frame_label.pack()
total_sales_label=Label(total_sales_frame,text=" Total Sales ",font=("times new roman",30,"bold"),bg="#E74C3C",fg="WhiteSmoke")
total_sales_label.pack()

total_sales_count_label=Label(total_sales_frame,text=" 0 ",font=("times new roman",30,"bold"),bg="#E74C3C",fg="WhiteSmoke")
total_sales_count_label.pack()

window.mainloop()