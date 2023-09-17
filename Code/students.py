from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import Button 
from tkinter import messagebox
import mysql.connector
import cv2

class Students: 
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Variables---------------------------------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_verification_ID = StringVar()
        self.var_std_name = StringVar()
        self.var_std_gender = StringVar()
        self.var_email = StringVar()
        self.var_std_phone = StringVar()
        self.var_std_roll = StringVar()
        

        
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

        #Frame
        main_frame = Frame(f_lbl1, bd = 2)
        main_frame.place(x=20, y=190, width=1480, height=580)

        #Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Details", font = ("times new roman", 19, "bold"))
        left_frame.place(x=10, y=10, width=720, height=550)

        #current course------------------------------------------------------
        curr_course_frame = LabelFrame(left_frame, bd=2, relief = RIDGE,  text = "Course Information", font = ("times new roman", 12, "bold"))
        curr_course_frame.place(x=5, y=10, width=700, height=130)

        #Dpeartment Combo--------------------------------------------
        dep_label = Label(curr_course_frame, text="Department", font = ("times new roman", 12, "bold"))
        dep_label.grid(row=0, column = 0, padx=10)

        dep_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_dep, font = ("times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"]=("Select Department", "CSE", "EEE", "ME")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        #Course Combo--------------------------------------------
        course_label = Label(curr_course_frame, text="Course", font = ("times new roman", 12, "bold"))
        course_label.grid(row=0, column = 3, padx=10)

        course_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_course, font = ("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"]=("Select Course", "CSE 2101", "CSE 2103", "EEE 2151")
        course_combo.current(0)
        course_combo.grid(row=0, column=4, padx=2, pady=10)

        #Year Combo--------------------------------------------
        year_label = Label(curr_course_frame, text="Year", font = ("times new roman", 12, "bold"))
        year_label.grid(row=1, column = 0, padx=10)

        year_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_year, font = ("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"]=("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

        #Semester Combo--------------------------------------------
        semester_label = Label(curr_course_frame, text="Semester", font = ("times new roman", 12, "bold"))
        semester_label.grid(row=1, column = 3, padx=10)

        semester_combo = ttk.Combobox(curr_course_frame, textvariable=self.var_semester, font = ("times new roman", 12, "bold"), width=17, state="readonly")
        semester_combo["values"]=("Select Semester", "1st", "2nd")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=4, padx=2, pady=10)

        #class student information
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information", font = ("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=150, width=700, height=350)

        #Student Verification ID--------------------------------------------
        studentID_label = Label(class_student_frame, text="Verification ID", font = ("times new roman", 12, "bold"))
        studentID_label.grid(row=0, column = 0, padx=10)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_verification_ID, width=15, font = ("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        #Student Name--------------------------------------------
        student_name_label = Label(class_student_frame, text="Student Name", font = ("times new roman", 12, "bold"))
        student_name_label.grid(row=0, column = 2, padx=10)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=15, font = ("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        #Student Gender--------------------------------------------
        student_gender_label = Label(class_student_frame, text="Student Gender", font = ("times new roman", 12, "bold"))
        student_gender_label.grid(row=1, column = 0, padx=10)

        # student_gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_gender, width=15, font = ("times new roman", 12, "bold"))
        # student_gender_entry.grid(row=1, column=1, padx=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_std_gender, font = ("times new roman", 12, "bold"), width=17, state="readonly")
        gender_combo["values"]=("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=2, pady=10)

        #Student Email--------------------------------------------
        student_email_label = Label(class_student_frame, text="Student Email", font = ("times new roman", 12, "bold"))
        student_email_label.grid(row=1, column = 2, padx=10)

        student_email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=15, font = ("times new roman", 12, "bold"))
        student_email_entry.grid(row=1, column=3, padx=10, sticky=W)

        #Student Phone Number--------------------------------------------
        student_phone_number_label = Label(class_student_frame, text="Student_Phone_Number", font = ("times new roman", 12, "bold"))
        student_phone_number_label.grid(row=2, column = 0, padx=10)

        student_phone_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_phone, width=15, font = ("times new roman", 12, "bold"))
        student_phone_number_entry.grid(row=2, column=1, padx=10, sticky=W)

        #Student Roll--------------------------------------------
        std_roll_label = Label(class_student_frame, text="Roll", font = ("times new roman", 12, "bold"))
        std_roll_label.grid(row=2, column = 2, padx=10)

        std_roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_roll, width=15, font = ("times new roman", 12, "bold"))
        std_roll_entry.grid(row=2, column=3, padx=10, sticky=W)

        #radio button
        self.var_radio1 = StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=4, column=0)

        self.var_radio2 = StringVar()
        radiobutton2=ttk.Radiobutton(class_student_frame, variable=self.var_radio2, text="No Photo Sample", value="No")
        radiobutton2.grid(row=4, column=1)

        #button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=20, y=150, width=600, height=100)

        #buttons
        save_btn = Button(btn_frame, command=self.add_data,text="Save", width=16, font = ("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=16, font = ("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=16, font = ("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=16, font = ("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=20, y=200, width=600, height=75)
        
        take_photo_sample_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=33, font = ("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_sample_btn.grid(row=0, column=0)

        update_photo_sample_btn = Button(btn_frame1, text="Update Photo Sample", width=33, font = ("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_sample_btn.grid(row=0, column=1)



        #Right Frame----------------------------------------------------------
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text = "Student Details", font = ("times new roman", 19, "bold"))
        right_frame.place(x=740, y=10, width=720, height=550)

        # search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        # search_frame.place(x=20, y=20, width=600, height=100)

        # search_label = Label(search_frame, text="Search By: ", font = ("times new roman", 12, "bold"), bg="green", fg="white")
        # search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # search_by_label = Label(search_frame, text="Select", font = ("times new roman", 12, "bold"))
        # search_by_label.grid(row=0, column = 1, padx=10)

        # search_by_combo = ttk.Combobox(search_frame, font = ("times new roman", 12, "bold"), width=17, state="readonly")
        # search_by_combo["values"]=("Select", "Roll No.", "Phone No.")
        # search_by_combo.current(0)
        # search_by_combo.grid(row=0, column=1, padx=2, pady=10)

        # search_entry = ttk.Entry(search_frame, width=20, font = ("times new roman", 12, "bold"))
        # search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # search_btn = Button(search_frame, text="Search", width=12, font = ("times new roman", 12, "bold"))
        # search_btn.grid(row=1, column=1)

        # showall_btn = Button(search_frame, text="Show All", width=12, font = ("times new roman", 12, "bold"))
        # showall_btn.grid(row=1 , column=2, padx=4)

        

        # -----------------Table Frame----------------------
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=30, width=680, height=450)

        scroll_x=ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient = VERTICAL)

        # self.student_table = ttk.Treeview(table_frame, columns=("Department", "Course", "Year", "Semester", "Student ID", "Name", "Gender", "Email", "Student Phone Number", "Guardian Phone Number", "Photo Sample"), xscrollcommand=scroll_x.set, yscrollcommand= scroll_y.set)
        self.student_table = ttk.Treeview(table_frame, columns=('Department', 'Course', 'Year', 'Semester', 'Verification_ID', 'Name', 'Gender', 'Email', 'Student_Phone_Number', 'Student_Roll', 'Photo_Sample'), xscrollcommand=scroll_x.set, yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Verification_ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Student_Phone_Number", text="Student_Phone_Number")
        self.student_table.heading("Student_Roll", text="Student_Roll")
        self.student_table.heading("Photo_Sample", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Verification_ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Student_Phone_Number", width=100)
        self.student_table.column("Student_Roll", width=100)
        self.student_table.column("Photo_Sample", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        
    #Functions----------------------------------------------

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_verification_ID=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else: 
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="123@abc", database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                            self.var_dep.get(), 
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(), 
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_verification_ID.get(), 
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_std_gender.get(), 
                                                                                                            self.var_email.get(),
                                                                                                            self.var_std_phone.get(), 
                                                                                                            self.var_std_roll.get(), 
                                                                                                            self.var_radio1.get()
                                                                                                            
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "All Information Saved")
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)



    # fetch data ---------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="123@abc", database="face_recognizer", auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data: 
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()



    #get cursor----------------------------
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_verification_ID.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_std_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_std_phone.set(data[8]),
        self.var_std_roll.set(data[9]),
        self.var_radio1.set(data[10])


    # Update Function-----------------------------------------------
    





    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_verification_ID=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want update this student details?", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="123@abc", database="face_recognizer", auth_plugin="mysql_native_password")
                    my_cursor=conn.cursor()
                    # Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, Email=%s, Student Phone Number=%s, Guardian Phone Number=%s, Photo Sample=%s, Student ID=%s
                    # my_cursor.execute('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s',(
                    #                                                                                         self.var_dep.get(), 
                    #                                                                                         self.var_course.get(),
                    #                                                                                         self.var_year.get(), 
                    #                                                                                         self.var_semester.get(),
                    #                                                                                         self.var_std_name.get(),
                    #                                                                                         self.var_std_gender.get(), 
                    #                                                                                         self.var_email.get(),
                    #                                                                                         self.var_std_phone.get(), 
                    #                                                                                         self.var_std_roll.get(), 
                    #                                                                                         self.var_radio1.get(),
                    #                                                                                         self.var_verification_ID.get()
                    #                                                                                     ))

                    my_cursor.execute("""
                                            UPDATE student
                                            SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, Email=%s, Student_Phone_Number=%s, Student_Roll=%s, Photo_Sample=%s
                                            WHERE Verification_ID=%s
                                        """, (
                                            self.var_dep.get(), 
                                            self.var_course.get(),
                                            self.var_year.get(), 
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_std_gender.get(), 
                                            self.var_email.get(),
                                            self.var_std_phone.get(), 
                                            self.var_std_roll.get(), 
                                            self.var_radio1.get(),
                                            self.var_verification_ID.get()
                                        ))


                else:
                    if not Update:
                        return
                messagebox.showinfo("Success",  "Student Details Successfully Updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:

                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    

    # Delete Function

    def delete_data (self):
        if self.var_verification_ID.get()=="":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student", "Do you want to delete all data of this student?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="123@abc", database="face_recognizer", auth_plugin="mysql_native_password")
                    my_cursor=conn.cursor()
                    sql = "DELETE FROM student where Verification_ID = %s"
                    val = (self.var_verification_ID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                


    # RESET FUNCTION

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_verification_ID.set("")
        self.var_std_name.set("")
        self.var_std_gender.set("Select")
        self.var_email.set("")
        self.var_std_phone.set("")
        self.var_std_roll.set("")
        self.var_radio1.set("")




    # Generate PHOTO SAMPLE--------------------------------------------------

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_verification_ID=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="123@abc", database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("""
                                            UPDATE student
                                            SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, Email=%s, Student_Phone_Number=%s, Student_Roll=%s, Photo_Sample=%s
                                            WHERE Verification_ID=%s
                                        """, (
                                            self.var_dep.get(), 
                                            self.var_course.get(),
                                            self.var_year.get(), 
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_std_gender.get(), 
                                            self.var_email.get(),
                                            self.var_std_phone.get(), 
                                            self.var_std_roll.get(), 
                                            self.var_radio1.get(),
                                            self.var_verification_ID.get()==id+1
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #Loading facedata from opencv-----------------------

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor =1.3 and Minimum Neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, img_frame = cap.read()
                    if face_cropped(img_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(img_frame), (450, 450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data set Completed!")
            
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


                











if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()