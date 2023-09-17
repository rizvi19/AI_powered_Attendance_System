from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import Button 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train: 
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")

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

        train_btn = Button(f_lbl1, text="Train", command=self.train_classifier, width=16, font = ("times new roman", 19, "bold"), bg="green", fg="white")
        train_btn.place(x=-3, y=300, width=1530, height=70)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')       #converting to Gray scale image
            imageNP = np.array(img, dtype=np.uint8)
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Train Data Set", imageNP)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #Train------------------------------------------

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed !!!")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


