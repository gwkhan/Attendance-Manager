# Attendance Manager CLI Project

import csv
import os

FILENAME = "attendance.csv"

def setup_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
    else:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:
                print("Last added:", rows[-1])

def add_attendance():
    data = input("Enter in format: Name, Date, Status (Present/Absent)\n")
    try:
        name, date, status = data.split(",")
        status = status.strip().capitalize()
        if status not in ["Present", "Absent"]:
            print("❌ Status must be 'Present' or 'Absent'")
            return
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name.strip(), date.strip(), status])
        print("Attendance saved.")
    except ValueError:
        print("❌ Invalid format. Use: Name, Date, Status")

def view_all():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_by_name():
    name = input("Enter name to search: ").strip().lower()
    found = False
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if name == row[0].strip().lower():
                print(row)
                found = True
    if not found:
        print("❌ Name not found.")

def show_attendance_percentage():
    name = input("Enter name to calculate attendance: ").strip().lower()
    total_days = 0
    present_days = 0
    absent_days = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if name == row[0].strip().lower():
                total_days += 1
                if row[2].strip().lower() == "present":
                    present_days += 1
                else:
                    absent_days += 1
    if total_days > 0:
        percent = present_days / total_days * 100
        print(f"✅ {name.title()} Attendance: {percent:.2f}%")
        print(f"Total entries: {total_days}, Present: {present_days}, Absent: {absent_days}")
    else:
        print("❌ No attendance records found for that name.")

def main():
    setup_file()
    while True:
        choice = input("\n1. Add Attendance\n2. View All\n3. Search by Name\n4. Show Attendance %\n5. Exit\nEnter: ")
        if choice == "1":
            add_attendance()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_by_name()
        elif choice == "4":
            show_attendance_percentage()
        elif choice == "5":
            print("Thank you for using the Universal Attendance Manager.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()