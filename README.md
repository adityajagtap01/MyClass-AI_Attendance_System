# 🎓 MyClass – AI Attendance System

MyClass is an AI-powered attendance management system that automates student attendance using multiple authentication methods including Face Recognition, Voice Recognition, and QR Code Attendance. The platform is designed for educational institutions to eliminate manual attendance, reduce proxy attendance, and maintain secure digital attendance records.

---

## 🚀 Features

### 👨‍🎓 Student Features
- Face ID Login
- Voice Enrollment
- QR Code Based Attendance
- View Enrolled Subjects
- View Attendance Records
- Join Subjects Using Subject Code
- Secure Profile Creation

### 👨‍🏫 Teacher Features
- Teacher Authentication
- Create & Manage Subjects
- Generate QR Attendance Sessions
- Face Recognition Attendance
- Voice Attendance
- Attendance Analytics
- Export Attendance Records

### 🤖 AI Features
- Face Recognition using Dlib Embeddings
- Voice Recognition using Speaker Embeddings
- Multi-Modal Attendance Verification
- Anti-Proxy Attendance Mechanism

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Streamlit

### Database
- Supabase
- PostgreSQL

### AI & Machine Learning
- Dlib
- Face Recognition Models
- Scikit-Learn
- NumPy
- Pandas

### QR Attendance
- Segno QR Generator

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 📸 Attendance Modes

### 1️⃣ Face Recognition Attendance
Students are identified using facial embeddings generated through Dlib's Face Recognition model.

### 2️⃣ Voice Recognition Attendance
Students can enroll their voice and mark attendance using voice authentication.

### 3️⃣ QR Code Attendance
Teachers generate a QR code session and students scan it to mark attendance instantly.

---

## 📂 Project Structure

```bash
MyClass/
│
├── app.py
├── landing_page/
│
├── src/
│   ├── components/
│   ├── Database/
│   ├── pipelines/
│   ├── screens/
│   ├── utils/
│   └── assets/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/MyClass.git
cd MyClass
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

## ▶️ Run Application

### Streamlit Application

```bash
streamlit run app.py
```

### Flask Landing Page

```bash
python app.py
```

---

## 📊 Advantages

- 100% Digital Attendance Records
- AI-Based Authentication
- Reduced Manual Work
- Faster Attendance Process
- Secure Student Identification
- Multiple Attendance Methods
- Cloud Database Storage

---

## 🎯 Future Enhancements

- Mobile Application
- Parent Dashboard
- Attendance Analytics Dashboard
- Email Notifications
- Live Classroom Monitoring
- Multi-Institution Support

---

## 👨‍💻 Developed By

**Aditya Jagtap**

Second Year Engineering Student  
Passionate about AI, Machine Learning, and Full Stack Development.

---

## 📜 License

This project is developed for educational and learning purposes.

© 2026 MyClass – AI Attendance System
