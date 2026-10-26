
from datetime import date

PISCINE_START = date(2027, 2, 8)


def show_schedule(shift):
    schedules = {
        "1": {
            "name": "Early shift (6:30-13:30)",
            "blocks": [
                ("05:00-06:15", "Wake,Commute to work: U-Bahn + bus"),
                ("06:15-06:30", "Arrive and prepare"),
                ("06:30-13:30", "Work"),
                ("13:30-14:30", "Commute home"),
                ("14:30-15:00", "Lunch and recovery"),
                ("15:00-16:00", "C lesson: learn one concept"),
                ("16:00-16:15", "Break"),
                ("16:15-17:15", "Code from memory"),
                ("17:15-18:15", "Gym"),
                ("18:15-19:00", "Shower and dinner"),
                ("19:00-19:45", "Timed exercise and mistake review"),
                ("19:45-20:45", "Commute"),
                ("20:45 onward", "Free time and wind down"),
            ],
        },
        "2": {
            "name": "Midshift (09:00-17:00)",
            "blocks": [
                ("07:00-07:30", "Wake up and breakfast"),
                ("07:30-08:00", "Light C review"),
                ("08:00-09:00", "Commute to work"),
                ("09:00-17:00", "Work"),
                ("17:00-18:00", "Commute home"),
                ("18:00-18:30", "Meal and recovery"),
                ("18:30-19:30", "Gym"),
                ("19:30-20:00", "Shower and dinner"),
                ("20:00-21:00", "C programming practice"),
                ("21:00-21:15", "Review mistakes"),
                ("21:15 onward", "Free time and wind down"),
            ],
        },
        "3": {
            "name": "Late shift (14:00-22:00)",
            "blocks": [
                ("07:30-08:00", "Wake up and breakfast"),
                ("08:00-09:00", "C lesson and examples"),
                ("09:00-09:15", "Break"),
                ("09:15-10:45", "Independent coding exercises"),
                ("10:45-11:00", "Break"),
                ("11:00-12:00", "Gym"),
                ("12:00-12:45", "Shower and lunch"),
                ("12:45-13:00", "Prepare for work"),
                ("13:00-14:00", "Commute to work"),
                ("14:00-22:00", "Work"),
                ("22:00-23:00", "Commute home"),
                ("After 23:00", "Wind down and sleep"),
            ],
        },
    }

    selected = schedules.get(shift)

    if selected is None:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    print("\nYour schedule:", selected["name"])
    print("-" * 55)

    for time, task in selected["blocks"]:
        print(f"{time:18} {task}")

    print("-" * 55)


today = date.today()
days_left = (PISCINE_START - today).days

print("=" * 55)
print("       42 BERLIN PISCINE TRAINING PLANNER")
print("=" * 55)
print(f"Today's date: {today.strftime('%d %B %Y')}")
print(f"Piscine starts: {PISCINE_START.strftime('%d %B %Y')}")
print(f"Days until Piscine: {days_left}")
print()
print("Choose your work shift:")
print("1. Early shift  (06:30-13:30)")
print("2. Midshift     (09:00-17:00)")
print("3. Late shift   (14:00-22:00)")

choice = input("\nEnter 1, 2, or 3: ").strip()
show_schedule(choice)
