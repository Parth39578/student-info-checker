# 📘 Student Information Finder
# This program returns details of a student based on name and roll number.

# Taking user input
name = input('Enter student name: ')
roll = int(input("Enter your roll number: "))

# Check for student details
if name == "Parth" and roll == 14160523:
    info = {
        "Name": "Parth",
        "Marks": "100",
        "Roll Number": "14160523",
        "Mother's Name": "Sangeeta Sharma"
    }
    print("\nHello Parth, here is your information:")
    print(info)

elif name == "Drishti" and roll == 1461989:
    info = {
        "Name": "Drishti",
        "Marks": "90",
        "Roll Number": "1461989",
        "Mother's Name": "Ruchi Gupta"
    }
    print("\nHello Drishti, here is your information:")
    print(info)

elif name == "Tarun" and roll == 14617798:
    info = {
        "Name": "Tarun",
        "Marks": "92",
        "Roll Number": "14617798",
        "Mother's Name": "Anjali"
    }
    print("\nHello Tarun, here is your information:")
    print(info)

else:
    print("\n❌ Sorry, system can't recognize the student.")










