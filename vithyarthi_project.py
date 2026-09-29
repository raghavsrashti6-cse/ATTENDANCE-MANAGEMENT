
#ATTENDANCE MANAGEMENTSTUDENT SYSTEM

students = {}


def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
    else:
        students[name] = [0, 0]   
        print("Student added!")
 



def mark_attendance():
    if len(students) == 0:
        print("No students added yet!")
        return

    for name in students:
        status = input(name + " (P/A): ").upper()

        if status == "P":
            students[name][0] += 1
        elif status == "A":
            students[name][1] += 1
        else:
            print("Invalid input! Enter P or A.")

    print("Attendance marked!")





def show_attendance():
    if len(students) == 0:
        print("No students added yet!")
        return

    print("\n==== ATTE    NDANCE ====")

    for name in students:
        present = students[name][0]
        absent = students[name][1]

        total = present + absent

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0



        print("\nStudent:", name)
        print("Present:", present)
        print("Absent:", absent)
        print("Attendance:", percentage, "%")




def main():
    while True:
        print("\n==== ATTENDANCE SYSTEM ====")
        print("1. Add student")
        print("2. Mark attendance")
        print("3. Show attendance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            show_attendance()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")





# Start the program
main()

##eligible for exams or not
attendance=int(input("enter attendance percetage: "))
if attendance>=75:
    print("eligible")
else:
    print("not eligible")
