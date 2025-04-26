import streamlit as st
import pandas as pd
import sqlite3
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText
import time
import os

conn = sqlite3.connect('attendance.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        status TEXT
    )
''')
conn.commit()

selected = option_menu(
    menu_title="Attendance App",
    options=["Home", "Admin Dashboard"],
    icons=["house", "gear"],
    menu_icon="cast",
    default_index=0,
)

def play_beep():
    try:
        duration = 1000 
        freq = 440  
        if os.name == 'nt':  
            import winsound
            winsound.Beep(freq, duration)
        else:  
            os.system('play -nq -t alsa synth {} sine {}'.format(duration/1000, freq))
    except Exception as e:
        st.error(f"Beep failed: {e}")

if selected == "Home":
    st.title("🎯 Attendance Alert App")

    name = st.text_input("Enter your Name:")
    date = st.date_input("Select Date:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Mark Present"):
            if not name:
                st.error("⚠️ Please enter your name first!")
            else:
                
                c.execute('SELECT * FROM attendance WHERE name = ? AND date = ?', (name, date))
                existing = c.fetchone()

                if existing:
                    st.error("❌ You have already marked attendance for this date!")
                else:
                    c.execute('INSERT INTO attendance (name, date, status) VALUES (?, ?, ?)', (name, date, "Present"))
                    conn.commit()
                    st.success(f"✅ {name} marked Present on {date}")

    with col2:
        if st.button("❌ Mark Absent"):
            if not name:
                st.error("⚠️ Please enter your name first!")
            else:
                
                c.execute('SELECT * FROM attendance WHERE name = ? AND date = ?', (name, date))
                existing = c.fetchone()

                if existing:
                    st.error("❌ You have already marked attendance for this date!")
                else:
                    c.execute('INSERT INTO attendance (name, date, status) VALUES (?, ?, ?)', (name, date, "Absent"))
                    conn.commit()
                    st.success(f"✅ {name} marked Absent on {date}")

    if st.button("📊 Check My Attendance"):
        if not name:
            st.error("⚠️ Please enter your name first!")
        else:
            df = pd.read_sql_query('SELECT * FROM attendance WHERE name = ?', conn, params=(name,))
            if not df.empty:
                total = len(df)
                presents = len(df[df["status"] == "Present"])
                percentage = (presents / total) * 100
                st.info(f"📈 Your attendance rate: {percentage:.2f}%")

                if percentage < 75:
                    st.warning("⚠️ ALERT: Attendance below 75%! Immediate action needed!")
                    play_beep()

                    flash_placeholder = st.empty()

                    for _ in range(5):
                        flash_placeholder.error("🚨 ATTENDANCE WARNING 🚨")
                        time.sleep(0.3)
                        flash_placeholder.empty()
                        time.sleep(0.3)

                    flash_placeholder.empty()
            else:
                st.error("⚠️ No attendance record found. Please mark your attendance first!")

elif selected == "Admin Dashboard":
    st.title("📋 Admin Dashboard")
    df = pd.read_sql_query('SELECT * FROM attendance', conn)

    if df.empty:
        st.warning("⚠️ No attendance records yet.")
    else:
        st.dataframe(df)

        stats = df.groupby('name')['status'].value_counts().unstack().fillna(0)
        st.subheader("📈 Overall Attendance Stats")
        st.dataframe(stats)