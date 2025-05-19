from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql




def connect_database():
    try:
        connection = pymysql.connect(host='localhost', user='root', password="1234" )
        cursor = connection.cursor()
        
    except Exception as e:
        messagebox.showerror("Database Connection Error", f"Error connecting to database:\n{e}")
        return None,None
    
    # Create database if not exists
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_systems')
    cursor.execute('USE inventory_systems')
    # Create employee table with all required fields
    cursor.execute(' CREATE TABLE IF NOT  EXISTS employee_data (  empid INT PRIMARY KEY,  name VARCHAR(100), email VARCHAR(100),gender VARCHAR(10),dob VARCHAR(20),employee_type VARCHAR(50),education VARCHAR(50),salary FLOAT,address TEXT,workshift VARCHAR(20),doj VARCHAR(20),contact VARCHAR(20),user_type VARCHAR(20),password VARCHAR(100))')
    # Removed recursive call to avoid infinite recursion

    return connection,cursor
   
   

    # Add this code where you want to test the connection
 
def save_employee(empid, name, email, gender, dob, employee_type, 
                education, salary, address, workshift, doj, 
                contact, user_type,password):
    

 if( empid==''or gender==''or employee_type==''or address=='' or email=='' or contact==''or dob=='' or name=='' or password==''or doj=='' or 
 education=="" or salary==''or workshift==" " or user_type==''):
    messagebox.showerror('Error','all field are required')

 else:
     
     connection,cursor=connect_database()
     if not cursor or not connection:
        return
     sql="INSERT DATA INTO employee_data VALUES(%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)"
     val=('empid', 'name', 'email', 'gender', 'dob', 'employee_type', 
                'education', 'salary', 'address', 'workshift', 'doj', 
                'contact', 'user_type','password')
                
     cursor.execute(sql,val)  

     connection.commit()
     messagebox.showinfo("Success","insert is successful")       
       






 
    


def employee_form(window):
    
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

    search_button=Button(search_frame,font=("times new roman",12,'bold'),cursor='hand2',text="Search",bg="SteelBlue4",width=10)
    search_button.grid(row=0,column=2,padx=30)

    show_button=Button(search_frame,font=("times new roman",12,"bold"),cursor='hand2',text="Show All",bg="SteelBlue4",width=10)
    show_button.grid(row=0,column=3,padx=30)

    # Create scrollbars
    HORIZONTAL_scrollbar = Scrollbar(Top_frame, orient=HORIZONTAL)
    VERTICAL_scrollbar = Scrollbar(Top_frame, orient=VERTICAL)

    # Create treeview with scrollbar configuration
    employee_treeview = ttk.Treeview(
        Top_frame, 
        columns=('empid', 'name', 'email', 'gender', 'dob', 'employee_type', 
                'education', 'salary', 'address', 'workshift', 'doj', 
                'contact', 'user_type','password'),
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
    employee_treeview.column('password', width=100)
    employee_treeview.pack(fill=BOTH, expand=True, padx=20, pady=20)

    #----------- details frame --------------------------------------------
    details_frame = Frame(employee_form, bd=1)
    details_frame.place(x=0, y=350 ,relwidth=1)

    EmpID = Label(details_frame, text="Empid", font=("times new roman", 15, "bold"),anchor='w')
    EmpID.grid(row=0, column=0, padx=20, pady=12,sticky='w')

    EmpID_entry = Entry(details_frame, font=("times new roman", 14, "bold"), bg='lightyellow')
    EmpID_entry.grid(row=0, column=1, padx=20, pady=12)

    Gender_label = Label(details_frame, text='Gender', font=("times new roman", 15, 'bold'),anchor='w')
    Gender_label.grid(row=1, column=0, padx=20, pady=12,sticky='w')

    Gender_combo = ttk.Combobox(details_frame, values=('Male', 'Female'), font=('times new roman', 14), state='readonly')
    Gender_combo.set('Gender')
    Gender_combo.grid(row=1, column=1, padx=20, pady=12)

    employee_type_label = Label(details_frame, text='Employee Type', font=("times new roman", 15, 'bold'),anchor='w')
    employee_type_label.grid(row=2, column=0, padx=20, pady=12,sticky='w')

    Employee_type_combo = ttk.Combobox(details_frame, values=('Full time', 'Trainer', 'Contract'), font=('times new roman', 14), state='readonly')
    Employee_type_combo.set('Full time')
    Employee_type_combo.grid(row=2, column=1, padx=20, pady=12)

    employee_Address_Label = Label(details_frame, text='Address', font=("times new roman", 15, 'bold'),anchor='w')
    employee_Address_Label.grid(row=3, column=0, padx=20, pady=12,sticky='w')

    employee_Address_Entry = Text(details_frame, font=("times new roman", 14, "bold"), bg='lightyellow', height=3, width=20)
    employee_Address_Entry.grid(row=3, column=1, padx=20, pady=12)

    

    employee_name_label = Label(details_frame, text="Name", font=("times new roman", 15, "bold"),anchor='w')
    employee_name_label.grid(row=0, column=2, padx=20, pady=12,sticky='w')

    employee_Name_Entry = Entry(details_frame, font=("times new roman", 14,), bg='lightyellow')
    employee_Name_Entry.grid(row=0, column=3, padx=20, pady=12)


    employee_email_label = Label(details_frame, text="Email", font=("times new roman", 15, "bold"),anchor='w')
    employee_email_label.grid(row=0, column=4, padx=20, pady=12,sticky='w')

    employee_email_Entry = Entry(details_frame, font=("times new roman", 14,), bg='lightyellow')
    employee_email_Entry.grid(row=0, column=5, padx=20, pady=12)


    employee_contact_label = Label(details_frame, text="Contact", font=("times new roman", 15, "bold"),anchor='w')
    employee_contact_label.grid(row=1, column=4, padx=20, pady=12,sticky='w')

    employee_contact_Entry = Entry(details_frame, font=("times new roman", 14,), bg='lightyellow')
    employee_contact_Entry.grid(row=1, column=5, padx=20, pady=12)


    
    employee_salary_label = Label(details_frame, text="Salary", font=("times new roman", 15, "bold"),)
    employee_salary_label.grid(row=2, column=4, padx=20, pady=12,sticky='w')

    employee_salary_Entry = Entry(details_frame, font=("times new roman", 14,), bg='lightyellow')
    employee_salary_Entry.grid(row=2, column=5, padx=20, pady=12)

    Work_shift_label = Label(details_frame, text='Work Shift', font=("times new roman", 15, 'bold'),anchor='w')
    Work_shift_label.grid(row=3, column=4, padx=20, pady=12,sticky='w')

    Work_shift_combo = ttk.Combobox(details_frame, values=('Day', 'Night'), font=('times new roman', 13), state='readonly',width=18)
    Work_shift_combo.set('Day')
    Work_shift_combo.grid(row=3, column=5, padx=20, pady=12)




    employee_Password_label = Label(details_frame, text="Password", font=("times new roman", 15, "bold"),anchor='w')
    employee_Password_label.grid(row=4, column=4, padx=20,sticky='w')

    employee_Password_Entry = Entry(details_frame, font=("times new roman", 14,), bg='lightyellow')
    employee_Password_Entry.grid(row=4, column=5, padx=20)

  
    
    employee_DOB_label = Label(details_frame, text="DOB", font=("times new roman", 15, "bold"),anchor='w')
    employee_DOB_label.grid(row=1, column=2, padx=20,sticky='w')


    employee_DOB_Entry = DateEntry(details_frame, font=("times new roman", 14,),width=18,state='readonly',date_pattern='dd/mm/yyyy')
    employee_DOB_Entry.grid(row=1, column=3, padx=20)

    # Education field
    education_label = Label(details_frame, text="Education", font=("times new roman", 15, "bold"),anchor='w')
    education_label.grid(row=2, column=2, padx=20, pady=12,sticky='w')

    education_combo = ttk.Combobox(details_frame, 
                                 values=('Bachelors', 'Masters', 'PhD', 'Other'),
                                 font=('times new roman', 14),
                                 state='readonly',
                                 width=18)
    education_combo.set('Select Education')
    education_combo.grid(row=2, column=3, padx=20, pady=12)

    # Date of Joining field
    doj_label = Label(details_frame, text="Date of Joining", font=("times new roman", 15, "bold"),anchor='w')
    doj_label.grid(row=3, column=2, padx=20, pady=12,sticky='w')

    doj_entry = DateEntry(details_frame,
                         font=("times new roman", 14),
                         width=18,
                         state='readonly',
                         date_pattern='dd/mm/yyyy')
    doj_entry.grid(row=3, column=3, padx=20, pady=12)

    # User Type field
    user_type_label = Label(details_frame, text="User Type", font=("times new roman", 15, "bold"),anchor='w')
    user_type_label.grid(row=4, column=2, padx=20, pady=12,sticky='w')

    user_type_combo = ttk.Combobox(details_frame,
                                  values=('Admin', 'Employee'),
                                  font=('times new roman', 14),
                                  state='readonly',
                                  width=18)
    user_type_combo.set('Select User Type')
    user_type_combo.grid(row=4, column=3, padx=20, pady=12)

    bottom_frame= Frame(employee_form,bg='whiteSmoke',bd=1)
    bottom_frame.place(x=0,y=670,height=50,relwidth=1)

    button_frame=Frame(bottom_frame,bg='whiteSmoke')
    button_frame.pack()

 #button 
    save_button = Button( button_frame, text="Save", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2",width=15,command=lambda:save_employee(EmpID_entry.get(),employee_Name_Entry.get(),employee_email_Entry.get(),Gender_combo.get(),employee_DOB_Entry.get(),employee_contact_Entry.get(),Employee_type_combo.get(),education_combo.get(),employee_salary_Entry.get(),employee_Address_Entry.get(1.0,END),doj_entry.get(),Work_shift_combo.get(),user_type_combo.get(),employee_Password_Entry.get()))
    save_button.grid(row=0,column=0,padx=50)

    update_button = Button( button_frame, text="Update", font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2",width=15)
    update_button.grid(row=0,column=1,padx=50)

    delete_button = Button( button_frame, text="Delete", font=("times new roman", 15, "bold"), bg="red", fg="white", cursor="hand2",width=15)
    delete_button.grid(row=0,column=2,padx=50)

    clear_button = Button( button_frame, text="Clear", font=("times new roman", 15, "bold"), bg="orange", fg="white", cursor="hand2",width=15)
    clear_button.grid(row=0,column=3,padx=50)