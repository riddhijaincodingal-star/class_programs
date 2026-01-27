import datetime

holidays = [
    "2026-01-26",
    "2026-08-15",
    "2026-10-02",
    "2026-12-25"
]

date_input = input("Enter date (YYYY-MM-DD): ")
date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

# Check weekend (Saturday=5, Sunday=6)
if date_obj.weekday() in (5, 6):
    print("🎉 Weekend! School holiday.")
elif date_input in holidays:
    print("🎉 It is a school holiday.")
else:
    print("📚 It is a working school day.")
