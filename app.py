
#login
from functools import wraps
#login required function

# Restrict access to logged-in users only
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

#Database
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
#just added 10/22/2025


##
from flask import Flask, render_template, Response, request, redirect, url_for
from ultralytics import YOLO
import cv2, os, numpy as np

app = Flask(__name__)
#smart key
app.secret_key = 'smartvision_secret_key'

#Database connection
app.secret_key = 'smartvision_secret_key'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # leave empty unless you set one in XAMPP
    database="smartvision_db"
)
cursor = db.cursor(dictionary=True)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model = YOLO('yolov8n.pt')
video_source = 0
mode_type = "object"
#other routes
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        flash('Account created successfully! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['username'] = username  #  Save username in session
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Try again.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

#ended
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/object')
@login_required
def object_detect():
    global mode_type
    mode_type = "object"
    return render_template('object.html')

@app.route('/lane')
@login_required
def lane_detect():
    global mode_type
    mode_type = "lane"
    return render_template('lane.html')

@app.route('/set_source', methods=['POST'])
@login_required
def set_source():
    global video_source
    mode = request.form.get('mode')
    if mode == 'stream':
        video_source = 0
    elif mode == 'upload':
        file = request.files.get('video')
        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            video_source = path
    return redirect(request.referrer)
#just added 10/21/2025
def generate_frames():
    global video_source, mode_type
    cap = cv2.VideoCapture(video_source)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        if mode_type == "object":
            results = model(frame, stream=True)
            for r in results:
                for box in r.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    label = f"{model.names[cls]} {conf:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        elif mode_type == "lane":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blur, 50, 150)
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=50)
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)
            cv2.putText(frame, "Lane & Curve Detection Active", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
##
#just added
from flask import Response

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#

if __name__ == '__main__':
    app.run(debug=True)
#Login Protection Decorator
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
