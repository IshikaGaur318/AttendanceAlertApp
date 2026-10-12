# 🎯 Attendance Alert App

A Python-based attendance management application built with **Streamlit, SQLite, and Pandas**. The app allows users to mark attendance, track attendance percentages, and receive warnings when their attendance falls below the required 75% threshold.

## ✨ Features

* ✅ **Mark Attendance:** Record daily attendance as Present or Absent.
* 📅 **Date Selection:** Select the date for attendance records.
* 🚫 **Duplicate Prevention:** Prevents multiple attendance entries for the same person on the same date.
* 📊 **Attendance Tracking:** Calculate and display individual attendance percentages.
* ⚠️ **Low Attendance Alerts:** Displays a warning when attendance falls below 75%.
* 🔔 **Beep Alert:** Includes an attempted sound alert for low attendance.
* 🗄️ **SQLite Database:** Stores attendance records persistently.
* 🛠️ **Admin Dashboard:** View attendance records and overall attendance statistics.
* 🖥️ **Interactive UI:** Simple and user-friendly interface built with Streamlit.

## 🛠️ Tech Stack

| Technology             | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| Python                 | Core application logic                     |
| Streamlit              | Interactive web interface                  |
| SQLite                 | Attendance data storage                    |
| Pandas                 | Data processing and statistics             |
| Streamlit Option Menu  | Navigation between application pages       |
| SMTP / Email Libraries | Imported for potential email functionality |

## 📁 Project Structure

```text
AttendanceAlertApp/
│
├── app.py          # Main application
├── attendance.db   # SQLite database
├── attendance.csv  # Attendance data file
└── README.md       # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/IshikaGaur318/AttendanceAlertApp.git
```

### 2. Navigate to the project directory

```bash
cd AttendanceAlertApp
```

### 3. Install the required dependencies

```bash
python3 -m pip install streamlit pandas streamlit-option-menu
```

### 4. Run the application

```bash
python3 -m streamlit run app.py
```

### 5. Open the application

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🚀 How to Use

1. Open the Attendance Alert App in your browser.
2. Enter your name and select the attendance date.
3. Click **Mark Present** or **Mark Absent**.
4. Click **Check My Attendance** to view your attendance percentage.
5. If your attendance falls below 75%, the application displays a warning.
6. Open **Admin Dashboard** to view stored attendance records and statistics.

## 📈 Attendance Calculation

The application calculates attendance percentage using the following formula:

```text
Attendance Percentage =
(Present Days / Total Recorded Days) × 100
```

For example, if a student is present for 7 out of 11 recorded days:

```text
(7 / 11) × 100 = 63.64%
```

Since the percentage is below 75%, the application displays a low-attendance warning.

## 🗄️ Database

The application uses SQLite to store attendance records.

Each record contains:

* `id` — Unique record identifier
* `name` — Student or user's name
* `date` — Attendance date
* `status` — Present or Absent

The database table is created automatically when the application starts.

## 🔮 Future Improvements

* 📧 Implement email notifications for low attendance.
* 🔐 Add secure authentication and role-based admin access.
* 👥 Support multiple students and class management.
* 📉 Add attendance charts and monthly reports.
* 📤 Enable CSV and Excel report exports.
* ☁️ Deploy the application online.
* 🧪 Add automated tests and input validation.

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python application development
* Building interactive web applications with Streamlit
* SQL database operations using SQLite
* Data analysis and calculations using Pandas
* Conditional logic and validation
* Creating dashboard-style interfaces





