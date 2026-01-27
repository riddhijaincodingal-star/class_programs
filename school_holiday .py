# School Holiday Checker

holidays = [
    "2026-01-26",  # Republic Day
    "2026-08-15",  # Independence Day
    "2026-10-02",  # Gandhi Jayanti
    "2026-12-25"   # Christmas
]

date = input("Enter date (YYYY-MM-DD): ")

if date in holidays:
    print("🎉 It is a school holiday!")
else:
    print("📚 It is a working school day.")
