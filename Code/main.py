from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import Button
from tkinter import messagebox
import os
from students import Students
from train import Train
from face_recognition import Recognition
from attendance import Attendance


class Face_Recognition: 
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        

        #LowerBack 
        img1 = Image.open(r"Images\Back.png")
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


        # Homepage Buttons

        # Attendance Button
        b1 = Button(f_lbl1, text = "Attendance", command=self.att, cursor = "hand2", font = ("times new roman", 27, "bold"), bg = "#242c37", fg = "white")
        b1.place(x=480, y=250, height=75, width=250)

        
        # Student Details Button
        b2 = Button(f_lbl1, text = "Student Details", command=self.student_details, cursor = "hand2", font = ("times new roman", 27, "bold"), bg = "#242c37", fg = "white")
        b2.place(x=480, y=350, height=75, width=250)

        
        # Face Detector Button
        b4 = Button(f_lbl1, text = "Face Detector", command=self.recognition, cursor = "hand2", font = ("times new roman", 27, "bold"), bg = "#242c37", fg = "white")
        b4.place(x=810, y=250, height=75, width=250)

        
        # Train Data Button
        b5 = Button(f_lbl1, text = "Train Data", command=self.train_data, cursor = "hand2", font = ("times new roman", 27, "bold"), bg = "#242c37", fg = "white")
        b5.place(x=810, y=350, height=75, width=250)

        
        # Photos Button
        b6 = Button(f_lbl1, text = "All Photos", command=self.open_img, cursor = "hand2", font = ("times new roman", 27, "bold"), bg = "#242c37", fg = "white")
        b6.place(x=645, y=450, height=75, width=250)


        # Exit Button
        b8 = Button(f_lbl1, text = "Exit", cursor = "hand2", command=self.iExit, font = ("times new roman", 27, "bold"), bg = "#242c37", fg = "red")
        b8.place(x=1400, y=700, height=40, width=75)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit= messagebox.askyesno("Exit", "Are you sure to EXIT ?", parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    # Button Functions --------------------------------------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Students(self.new_window)

    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Recognition(self.new_window)

    def att(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

