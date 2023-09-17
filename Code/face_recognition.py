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

class Recognition: 
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

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

        recog_btn = Button(f_lbl1, text="Recognize Face", command=self.face_recog, cursor="hand2", width=16, font = ("times new roman", 19, "bold"), bg="green", fg="white")
        recog_btn.place(x=-3, y=300, width=1530, height=70)


    # function



    # For Attendance--------------------------------------

    def mark_attendance(self, fetch_ID, fetch_Roll, fetch_name, fetch_dep):
        with open("attendance_list.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((fetch_ID not in name_list) and (fetch_Roll not in name_list) and (fetch_name not in name_list) and (fetch_dep not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{fetch_ID}, {fetch_Roll}, {fetch_name}, {fetch_dep}, {dtString}, {d1}, Preset")






    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="123@abc", database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Verification_ID = " + str(id))
                fetch_name = my_cursor.fetchone()
                # fetch_name = "+".join(fetch_name)
                if fetch_name is not None:
                    fetch_name = fetch_name[0]

                my_cursor.execute("SELECT Student_Roll FROM student WHERE Verification_ID = " + str(id))
                fetch_Roll = my_cursor.fetchone()
                # fetch_ID = "+".join(fetch_ID)
                if fetch_Roll is not None:
                    fetch_Roll = fetch_Roll[0]

                my_cursor.execute("SELECT Department FROM student WHERE Verification_ID  = " + str(id))
                fetch_dep = my_cursor.fetchone()
                # fetch_dep = "+".join(fetch_dep)
                if fetch_dep is not None:
                    fetch_dep = fetch_dep[0]


                my_cursor.execute("SELECT Verification_ID FROM student WHERE Verification_ID  = " + str(id))
                fetch_ID = my_cursor.fetchone()
                # fetch_dep = "+".join(fetch_dep)
                if fetch_ID is not None:
                    fetch_ID = fetch_ID[0]


                if confidence>77:
                    cv2.putText(img, f"Roll: {fetch_Roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {fetch_name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {fetch_dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(fetch_ID, fetch_Roll, fetch_name, fetch_dep)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,h]

            return coord
        
        def recognition(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)

            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        # if not video_cap:
        #     print("Video did not cap")

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Didn't frame")
                continue
            img = recognition(img, clf, faceCascade)
            cv2.imshow("Welcome to RUET", img)

            # self.root.after(100, self.face_recog)

            # if not self.root.winfo_exists():
            #     break

            # self.root.update_idletasks()
            self.root.update()

            if cv2.waitKey(1)==27:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        # while True:
        #     try:
        #         ret, img = video_cap.read()
        #         if not ret:
        #             print("Error: Could not read frame from camera.")
        #             break
        #         img = recognition(img, clf, faceCascade)
        #         cv2.imshow("Welcome to RUET", img)

        #         root.update_idletasks()
        #         root.update()

        #         if cv2.waitKey(1) == 13 or root.protocol("WM_DELETE_WINDOW"):
        #             break
        #     except Exception as e:
        #         print("Error:", str(e))

        # video_cap.release()
        # cv2.destroyAllWindows()


        



            


if __name__ == "__main__":
    root = Tk()
    obj = Recognition(root)
    root.mainloop()