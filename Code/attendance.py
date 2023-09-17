from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import Button 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import filedialog
import csv
from pyparsing import delimited_list
my_data_of_csv=[]

class Attendance: 
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        #Variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #LowerBack 
        img1 = Image.open(r"Images\Background111.png")
        img1 = img1.resize((1530, 790), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label (self.root, image = self.photoimg1)
        f_lbl1.place(x=0, y=0, width=1530, height=790)

        title_lbl1 = Label(f_lbl1, text = "Rajshahi University of Engineering and Technology", font = ("times new roman", 35, "bold",), bg = "white", fg = "green")
        title_lbl1.place(x=0, y=130, width=1530, height=55)


        #RUET Logo
        ruetlogo = Image.open(r"Images\RUET_logo.png")
        ruetlogo = ruetlogo.resize((156, 130), Image.LANCZOS)
        self.logoimg1 = ImageTk.PhotoImage(ruetlogo)

        logo_lbl = Label (self.root, image = self.logoimg1)
        logo_lbl.place(x=687, y=0, width=156, height=130)

        # recog_btn = Button(f_lbl1, text="Recognize Face", command=self.face_recog, cursor="hand2", width=16, font = ("times new roman", 19, "bold"), bg="green", fg="white")
        # recog_btn.place(x=-3, y=300, width=1530, height=70)



        #Frame
        main_frame = Frame(f_lbl1, bd = 2)
        main_frame.place(x=20, y=190, width=1480, height=580)

        #Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Attendance", font = ("times new roman", 19, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=550)

        left_inside_frame = Frame(Left_frame,relief=RIDGE,bd=2,bg='white')
        left_inside_frame.place(x=0,y=135,width=725,height=370)

        #Labels and Entry:
        #Attendance ID
        attendanceID_label = Label(left_inside_frame,text='Attendance-ID:',font=('times new roman',13,'bold'),bg='white')
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=('times new roman',13,'bold'))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        roll_label = Label(left_inside_frame,text='Roll:',font=('times new roman',13,'bold'),bg='white')
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=('times new roman',13,'bold'))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        Name_label = Label(left_inside_frame,text='Name:',font=('times new roman',13,'bold'),bg='white')
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        Name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=('times new roman',13,'bold'))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Departement
        dep_label = Label(left_inside_frame,text='Department:',font=('times new roman',13,'bold'),bg='white')
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=('times new roman',13,'bold'))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        time_label = Label(left_inside_frame,text='Time:',font=('times new roman',13,'bold'),bg='white')
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=('times new roman',13,'bold'))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        date_label = Label(left_inside_frame,text='Date:',font=('times new roman',13,'bold'),bg='white')
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=('times new roman',13,'bold'))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance_Status:
        attendance_status_label = Label(left_inside_frame,text='Attendance Status:',font=('times new roman',13,'bold'),bg='white')
        attendance_status_label.grid(row=3,column=0,padx=10,sticky=W)

        attendance_status_combo=ttk.Combobox(left_inside_frame,font=('times new roman',13,'bold'),width=18,state='readonly')
        attendance_status_combo['values']=('Status','Present','Absent')
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3,column=1,padx=2,pady=10)

        #Buttons Frame:
        button_frame = Frame(left_inside_frame,bd=2,bg='white',relief=RIDGE)
        button_frame.place(x=0,y=300,width=720,height=35)

        import_btn=Button(button_frame,text='Import csv',command=self.import_csv_data,font=('times new roman',12,'bold'),bg='blue',fg='white',width=26)
        import_btn.grid(row=0,column=0)

        export_btn=Button(button_frame,text='Export csv',command=self.export_csv_data,font=('times new roman',12,'bold'),bg='blue',fg='white',width=26)
        export_btn.grid(row=0,column=1)

        reset_btn=Button(button_frame,text='Reset',command=self.reset_data,font=('times new roman',12,'bold'),bg='blue',fg='white',width=26)
        reset_btn.grid(row=0,column=2)







        #Right Frame----------------------------------------------------------
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Attendance Details", font = ("times new roman", 19, "bold"))
        Right_frame.place(x=740, y=10, width=720, height=550)

        table_frame = Frame(Right_frame,relief=RIDGE,bd=2,bg='white')
        table_frame.place(x=5,y=2,width=710,height=455)

         #Scroll Bar:
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)        

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id',text='Attendance-ID')
        self.AttendanceReportTable.heading('roll',text='Roll')
        self.AttendanceReportTable.heading('name',text='Name')
        self.AttendanceReportTable.heading('department',text='Department')
        self.AttendanceReportTable.heading('time',text='Time')
        self.AttendanceReportTable.heading('date',text='Date')
        self.AttendanceReportTable.heading('attendance',text='Attendance')

        self.AttendanceReportTable['show']='headings'

        #Setting width
        self.AttendanceReportTable.column('id',width=100)
        self.AttendanceReportTable.column('roll',width=100)
        self.AttendanceReportTable.column('name',width=100)
        self.AttendanceReportTable.column('department',width=100)
        self.AttendanceReportTable.column('time',width=100)
        self.AttendanceReportTable.column('date',width=100)
        self.AttendanceReportTable.column('attendance',width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind('<ButtonRelease>',self.get_cursor)




    # function


    def fetch_Data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('',END,values=i)

    #Import data
    def import_csv_data(self):
        global my_data_of_csv
        my_data_of_csv.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),('All File','*.*')),parent=self.root)
        with open(file_name) as myfile:
            csv_read=csv.reader(myfile)
            for i in csv_read:
                my_data_of_csv.append(i)
            self.fetch_Data(my_data_of_csv)


    #Export data
    def export_csv_data(self):
        try:
            if len(my_data_of_csv)<1:
                messagebox.showerror('No Data','No data found!!!',parent=self.root)
                return False
            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),('All File','*.*')),parent=self.root)
            with open(file_name,mode='w',newline='\n') as myfile:
                export_write=csv.writer(myfile)
                for i in my_data_of_csv:
                    export_write.writerow(i)
                messagebox.showinfo('Success','Your data exported to the file '+os.path.basename(file_name)+' successfully.')
        except Exception as es:
            messagebox.showerror('Error',f'Due to: {str(es)}',parent=self.root)


    #Function which will help to show the data from table to the entry fill:
    def get_cursor(self,event=''):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    
    #Function to reset data:
    def reset_data(self):
        self.var_atten_id.set('')
        self.var_atten_roll.set('')
        self.var_atten_name.set('')
        self.var_atten_dep.set('')
        self.var_atten_time.set('')
        self.var_atten_date.set('')
        self.var_atten_attendance.set('')



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()