# 🎓 Student Smart Campus AI Management System

An AI-powered, production-ready Student & Campus Management System built with **Python**, **Streamlit**, and custom **CSS glassmorphism**. Feature-packed with JSON file persistence, bcrypt authentication, audit activity tracking, Plotly analytical visualisations, and AI campus advisory reporting.

---

## 🚀 Features Overview

### 🔐 Authentication & Access Control
- **Secure Login**: Bcrypt-hashed password verification, show password toggle, remember me options, and administrative recovery links.
- **User Registration**: Real-time email validation, 10-15 digit phone validation, duplicate username checking, and password strength requirements.

### 📊 AI Campus Dashboard
- **Telemetry Cards**: Total Students, Active Users, Published Announcements, Department Notices.
- **AI Campus Advisor Report**: Intelligent analytics narrative examining average CGPA, attendance risk alerts (<75%), department density, and recommended actions.
- **Interactive Visualizations**: Plotly Department Distribution Pie/Donut charts and Year-Wise Enrolment Bar charts.
- **Dynamic Widgets**: Live Date & Time hero banner, recent activity timeline, latest announcement, and notice board highlights.

### 🎓 Student Profile Management
- **Add Student**: Form validation preventing duplicate Student IDs with email/phone regex enforcement.
- **Update Student**: Searchable student profile editor for real-time field updates.
- **Delete Student**: Confirmation prompt with permanent deletion and mandatory audit log recording.
- **Student Directory**: Multi-criteria search, department filter, year filter, sorting by CGPA/Attendance, interactive table, and single-click CSV export.

### 📢 Campus Announcements & 📌 Notice Board
- Priority-tagged campus announcements (High, Medium, Low) and departmental circulars with create, edit, and delete capability.

### 📜 Audit Trail & History
- Automated logging of logins, logouts, registration, student record mutations, and announcement/notice creation with exact date, time, and user attribution.

---

## 🛠️ Project Structure

```text
StudentSmartCampusAI/
│
├── app.py                     # Main Streamlit Application Entrypoint
├── requirements.txt           # Python Package Dependencies
├── runtime.txt                # Python Runtime Specification (3.12.4)
├── render.yaml                # Render Web Service Deployment Manifest
├── README.md                  # Project Documentation
│
├── assets/
│   ├── logo.png               # Campus AI Branding Logo
│   ├── background.jpg         # Hero & Wallpaper Visuals
│   └── style.css              # Custom Master CSS Stylesheet
│
├── database/
│   ├── users.json             # User Credentials (Bcrypt Hashed)
│   ├── students.json          # Enrolled Student Records
│   ├── announcements.json     # Campus Announcements
│   ├── notices.json           # Department Circulars
│   └── history.json           # Audit Logs & Action History
│
└── modules/
    ├── auth.py                # Authentication & Registration Engine
    ├── dashboard.py           # Dashboard Views & Analytics Widgets
    ├── students.py            # Student CRUD & Directory Operations
    ├── announcements.py       # Campus Announcement Manager
    ├── notices.py             # Department Notice Manager
    ├── history.py             # Audit Trail Renderer
    ├── database.py            # Crash-Proof JSON Read/Write Layer
    └── utils.py               # Input Regex, Security & AI Analytics
```

---

## 💻 Local Setup & Installation

### 1. Prerequisites
Ensure Python 3.10+ is installed on your system.

### 2. Clone / Download Repository
Navigate to the project root directory:
```bash
cd StudentSmartCampusAI
```

### 3. Install Dependencies
Install all required libraries:
```bash
pip install -r requirements.txt
```

### 4. Run Application
Launch the Streamlit web application:
```bash
streamlit run app.py
```

Default Seed Accounts for Quick Testing:
- **Admin**: `admin` / `password123`
- **Student**: `john_doe` / `password123`

---

## ☁️ Deployment on Render

This project is pre-configured for one-click deployment on [Render](https://render.com).

1. Push your repository to GitHub / GitLab.
2. Log into Render and click **New +** -> **Web Service**.
3. Connect your repository.
4. Render will automatically detect `render.yaml` or you can manually set:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
5. Click **Deploy Web Service**.
