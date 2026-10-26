
import streamlit as st
from datetime import date

PISCINE_START = date(2027, 2, 8)

st.set_page_config(
    page_title="My Schedule",
    page_icon="🎯",
    layout="centered",
)

st.markdown("""
<style>
.stApp {
    background-color: #123524;
    color: #F8FAFC;
}

h1, h2, h3, p, label {
    color: #F8FAFC;
}

div[data-testid="stMetric"] {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 12px;
}

div[data-testid="stMetricValue"] {
    color: #67E8F9;
}
</style>
""", unsafe_allow_html=True)

st.title("🎯 My Planner")
st.write("Prepare, one day at a time.")

today = date.today()
days_left = (PISCINE_START - today).days

st.metric("Days until Project", days_left)
st.write("**Project starts:** 8 February 2027")

st.divider()
st.header("Choose your work shift")

shift = st.selectbox(
    "Which shift are you working?",
    [
        "Early shift (06:30–13:30)",
        "Midshift (09:00–17:00)",
        "Late shift (14:00–22:00)",
    ],
)

schedules = {
    "Early shift (06:30–13:30)": [
        ("05:15–06:15", "Commute to work"),
        ("06:30–13:30", "Work"),
        ("13:30–14:30", "Commute home"),
        ("15:00–16:00", "Learn one C concept"),
        ("16:15–17:15", "Code from memory"),
        ("17:15–18:15", "Gym"),
        ("19:00–19:45", "Timed exercise and review"),
    ],
    "Midshift (09:00–17:00)": [
        ("07:30–08:00", "Review C"),
        ("08:00–09:00", "Commute to work"),
        ("09:00–17:00", "Work"),
        ("17:00–18:00", "Commute home"),
        ("18:30–19:30", "Gym"),
        ("20:00–21:00", "C programming practice"),
    ],
    "Late shift (14:00–22:00)": [
        ("08:00–09:00", "Learn one C concept"),
        ("09:15–10:45", "Independent coding exercises"),
        ("11:00–12:00", "Gym"),
        ("13:00–14:00", "Commute to work"),
        ("14:00–22:00", "Work"),
        ("22:00–23:00", "Commute home"),
    ],
}

st.subheader("Your daily plan")

for time, task in schedules[shift]:
    st.write(f"**{time}** — {task}")

st.divider()
st.caption("Small steps every day. Build your skills.")
