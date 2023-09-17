# AI_powered_Attendance_System
My RUET 2nd Year Odd Semester Software Development Project

## **Project Details** 

The AI-Powered Attendance System is a comprehensive software solution designed to streamline and automate attendance management processes in educational institutions like RUET. This system provides an efficient and accurate method for recording and tracking attendance.

**Key Features**

User-Friendly Interface: The system boasts an intuitive user interface developed using the Tkinter library in Python, making it accessible and easy to navigate for both administrators and users.

**Data Acquisition with Computer Vision**: The project incorporates computer vision technology, utilizing the OpenCV library, to capture and process facial data. The system extracts facial features, converts images to grayscale, and stores relevant information for recognition.

**Data Training and Storage**: The train.py module is responsible for training the system's machine learning model. It processes a dataset of facial images, extracting unique features and associating them with individuals. This trained model is saved for future recognition tasks.

**Real-time Face Recognition**: The face_recognition.py module utilizes the trained model to perform real-time face recognition. When individuals present themselves, the system identifies them, matches their features with stored data, and records attendance based on their recognition confidence.

**Attendance Management**: The attendance.py module provides a user-friendly attendance management interface. Administrators can input attendance manually or import data from CSV files. The system keeps a comprehensive record of attendance, including date, time, and student details.

**Export and Import Functionality**: Users can easily export attendance data to CSV files for record keeping or further analysis. Similarly, the system allows importing attendance data from CSV files, facilitating data entry and manipulation.

**Attendance Reports**: The system generates attendance reports in tabular form. These reports display student information, attendance status, date, and time, making it effortless for administrators to monitor and manage attendance records.

**Customizable Attendance Status**: The system supports customizable attendance status options, enabling administrators to define statuses like "Present," "Absent," or any other relevant categories.

**Security and Privacy**: Security is paramount in this system. User data, particularly facial images, is securely stored and accessed only for the purpose of attendance tracking. Access to the system is controlled through user authentication.

**Scalability**: The system can be easily scaled to accommodate larger institutions or organizations. Adding more users and expanding the database is a straightforward process.


*The Code*


# **main.py**


The "main.py" script serves as the central component of the AI-Powered Attendance System. This script is responsible for managing the overall flow of the application, including user interactions, data handling, and integration with the other components of the system.



**Key Features and Functionalities of main.py**

Graphical User Interface (GUI): The script utilizes the Tkinter library to create an intuitive and user-friendly interface for the application. This GUI allows users, typically educators or administrators, to interact with the system seamlessly.

**Navigation**: It provides navigation between different functionalities and sections of the application, such as data collection, face recognition, attendance management, and exporting data.

**Image Capture:** The script enables the capture of images for building the dataset used in face recognition. Users can specify student details and click a button to capture facial images.

**Data Management**: main.py manages the storage and retrieval of student data, including their names, roll numbers, and departments. This data is crucial for associating recognized faces with specific students.

**Real-time Face Recognition:** It integrates with the face recognition component to recognize and verify the identity of students during attendance marking. Real-time video feeds from a camera are used for this purpose.

**Attendance Marking**: Users can mark attendance for individual students by clicking on their recognized faces. The system records the time and date of attendance.

**Data Export**: The script facilitates the export of attendance data to CSV files, allowing easy integration with other record-keeping systems.

** *Purpose* **

The primary purpose of "main.py" is to provide an intuitive interface for users to interact with the AI-Powered Attendance System. It streamlines the process of data collection, face recognition, and attendance management, ultimately improving the efficiency and accuracy of attendance tracking in educational institutions.

 # **student.py**


The "student.py" script plays a pivotal role in the AI-Powered Attendance System as it manages student data and serves as a bridge between the system's database and the attendance recording process.

**Key Features and Functionalities of student.py**

**Student Data Management**: "student.py" is responsible for maintaining a comprehensive database of student information. It includes essential details such as student ID, name, roll number, department, and unique verification ID.

**Database Connectivity**: The script establishes a connection with the system's database, facilitating the retrieval and storage of student data. It utilizes MySQL as the database management system.

**Data Retrieval**: "student.py" allows the system to retrieve student data based on verification IDs. This feature is crucial for associating recognized individuals with their respective student profiles.

**Data Validation**: It ensures the accuracy and integrity of student data. The script validates student information before it is used for attendance logging, preventing erroneous or incomplete records.

**Data Presentation**: "student.py" presents student information in a structured format, making it easily accessible for other system components. This includes displaying student names, roll numbers, and departments.

**Integration with Attendance**: The script integrates seamlessly with the attendance recording process. It supplies the necessary student details to the main system, ensuring that each attendance record is associated with the correct student.

**Error Handling:** "student.py" includes error-handling mechanisms to address potential issues with database connectivity and data retrieval. It ensures the system operates reliably and efficiently.

**Security**: Student data is handled securely to protect sensitive information. The script incorporates security measures to prevent unauthorized access to student records.

** *Purpose* **

The "student.py" script in the AI-Powered Attendance System serves the purpose of managing student data efficiently. It connects to the system's database, retrieves student information, validates it, and integrates it seamlessly with the attendance recording process. This script ensures the accuracy and security of student records, contributing to the system's overall functionality and reliability.


# **train.py**


The "train.py" script is a vital component of the AI-Powered Attendance System, specifically focused on the training of the facial recognition model. This script is responsible for processing and preparing the dataset, training the machine learning model, and saving it for later use in real-time face recognition.

**Key Features and Functionalities of train.py**

**Data Preprocessing**: The script begins by preprocessing the dataset of facial images. It converts the images to grayscale, making them suitable for machine learning, and extracts essential information such as student IDs.

**Dataset Preparation:** It collects and organizes facial images along with corresponding student IDs. This prepared dataset is crucial for training the machine learning model to recognize individual faces.

**Model Training**: "train.py" employs the OpenCV library to train a machine learning model, specifically the LBPH (Local Binary Pattern Histogram) Face Recognizer. The model learns to identify students' faces based on the prepared dataset.

**Model Saving:** Once the model is trained, it is serialized and saved as "classifier.xml." This saved model can be used for real-time face recognition during attendance marking.

**User Notification**: After successful training, the script provides a notification to the user, indicating the completion of the training process.

** *Purpose* ** 

The primary purpose of "train.py" is to facilitate the training of the facial recognition model, which is a critical component of the AI-Powered Attendance System. By processing the dataset and training the model, this script enables the system to accurately identify and verify students' faces during attendance marking.

# **face_recognition.py**


The "face_recognition.py" script is a pivotal component of the AI-Powered Attendance System, responsible for real-time face recognition and attendance marking. This script utilizes the trained machine learning model to identify and verify students' faces during classroom attendance sessions.

**Key Features and Functionalities of face_recognition.py**

**Real-Time Face Recognition:** "face_recognition.py" utilizes the OpenCV library to capture video frames from a webcam or camera feed in real-time. It continuously analyzes these frames for the presence of faces.

**Trained Model Integration:** The script integrates the trained facial recognition model saved as "classifier.xml," which was prepared using the "train.py" script. This model is used to recognize students' faces.

**Face Detection:** It employs a Haar Cascade classifier to detect faces within each frame. Once a face is detected, the script proceeds to identify and verify it using the trained model.

**Recognition and Verification:** The facial recognition model predicts the student's identity based on the detected face. It calculates a confidence score to determine the accuracy of the prediction.

**Attendance Marking:** When a student's face is successfully recognized with high confidence, their attendance is marked as "Present" in the attendance record. The script captures the student's roll number, name, and department for logging.

**Unknown Faces Handling:** If a face is detected but cannot be confidently recognized, it is labeled as "Unknown Face." This helps identify individuals who may not be part of the registered student dataset.

**Database Integration:** The script connects to a MySQL database to fetch additional student information such as name, roll number, and department. This information is used for attendance marking and logging.

**User Interface**: While performing recognition, the script displays a graphical user interface (GUI) window that shows the video feed with bounding boxes around recognized faces and their associated information.

**Continuous Monitoring:** The script continually processes frames until the user manually terminates the attendance session.



**Purpose**

The primary purpose of "face_recognition.py" is to enable real-time face recognition and automated attendance marking. It leverages the previously trained machine learning model to identify students' faces, ensuring accurate attendance tracking.

# **attendance.py**


The "attendance.py" script serves as the user interface for the AI-Powered Attendance System, enabling administrators and educators to manage attendance records effectively. It provides an intuitive graphical interface for importing, exporting, and reviewing attendance data.

**Key Features and Functionalities of attendance.py**

**User-Friendly Interface:** "attendance.py" offers an intuitive and user-friendly interface, making it easy for administrators and educators to interact with the attendance system.

**Import Attendance Data:** Users can import attendance data from CSV files, facilitating the bulk addition of attendance records. This feature simplifies the process of recording attendance for large classes.

**Export Attendance Data:** The script allows users to export attendance records to CSV files. This functionality ensures that attendance data can be shared, analyzed, and stored for administrative and reporting purposes.

**Attendance Record Display:** It displays attendance records in a tabular format within the interface, providing details such as attendance ID, roll number, student name, department, time, date, and attendance status.

**Data Management:** Users can efficiently manage attendance records, including editing and deleting entries as needed. This ensures data accuracy and flexibility in managing attendance information.

**Reset Functionality:** "attendance.py" includes a reset function, allowing users to clear input fields and start fresh when recording new attendance data.

**Visual Components:** The script incorporates visual elements such as buttons, labels, and entry fields, enhancing the overall user experience and making it accessible to users with varying levels of technical expertise.

**Data Validation:** The system validates user input to ensure that attendance data is correctly formatted and consistent.

**Date and Time Stamping:** The script automatically timestamps attendance records with the current date and time, providing accuracy and accountability.

**Purpose**

The primary purpose of "attendance.py" is to offer a convenient and user-friendly interface for managing attendance data. It acts as a bridge between the automated attendance system and users, simplifying the process of importing, exporting, and reviewing attendance records.


# **Conclusion**

The AI-Powered Attendance System represents a modern and efficient solution for attendance management in educational institutions and organizations. Its integration of artificial intelligence and computer vision technologies guarantees accurate attendance tracking while providing a user-friendly interface for administrators and users. This project enhances efficiency, reduces errors, and ensures the security and privacy of attendance data.

