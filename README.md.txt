🧠 SmartVision: An Integrated Object, Lane, and Curve Detection System
📘 Overview

SmartVision is a web-based intelligent detection system designed to identify objects, lanes, and road curves in real time.
Developed as part of an academic project at Koforidua Technical University, the system integrates Artificial Intelligence (AI) and Computer Vision techniques to enhance road awareness, safety, and academic research.

SmartVision provides a unified platform that demonstrates how advanced models like YOLOv8 and OpenCV can work together within a web environment using Flask and MySQL.

🚗 Features

Object Detection: Identifies vehicles, pedestrians, and road signs in real-time using YOLOv8.

Lane Detection: Detects and highlights lane markings using edge and ROI-based image processing.

Curve Detection: Recognizes road curvature for navigation and awareness.

Live Video Streaming: Supports webcam or uploaded video feeds.

User Authentication: Includes basic login and signup functionality via MySQL database.

Educational Platform: Designed for students and researchers studying AI-based computer vision.

🧩 Tech Stack
Component	Technology Used
Programming Language	Python 3
Web Framework	Flask
Object Detection Model	YOLOv8
Image Processing	OpenCV
Database	MySQL (XAMPP)
Frontend	HTML, CSS
Environment	Localhost (XAMPP Server)
⚙️ System Architecture

The system follows a client–server model:

Frontend (Client): Web interface for uploading videos or streaming camera feed.

Backend (Server): Flask-based Python backend handles image processing, YOLOv8 model inference, and database operations.

Database: MySQL stores user login credentials and related session data.

💻 Installation and Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/SmartVision.git
cd SmartVision

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Start XAMPP

Open XAMPP Control Panel

Start Apache and MySQL

5️⃣ Configure Database

Open phpMyAdmin → create a database named smartvision

Import your user table or run the SQL provided in your project

6️⃣ Run the Application
python app.py


Then open your browser and go to:

http://127.0.0.1:5000

🧠 How It Works

User logs in or signs up through the authentication interface.

System accepts a video upload or activates the webcam for live detection.

YOLOv8 detects objects, while OpenCV detects lanes and curves.

Processed video frames are displayed in real-time through Flask’s video streaming.

📊 Results

Accurate detection of multiple road elements in real time.

Enhanced lane and curve recognition using Region of Interest (ROI) and smoothing techniques.

Smooth web interface optimized for both uploaded and live streams.

🚀 Future Improvements

Integrate system into vehicle hardware (Raspberry Pi, Jetson Nano).

Deploy to the cloud for remote access.

Add traffic sign recognition and voice alerts.

Replace MySQL with Oracle DB for enhanced scalability and security.

👩‍💻 Author

Name: Felix Torsu
Institution: Koforidua Technical University
Department: Computer Science
Supervisor: Professor Seth Okyere Danqwah
Year: 2025

🧾 License

This project is open-source and free to use for educational and research purposes.