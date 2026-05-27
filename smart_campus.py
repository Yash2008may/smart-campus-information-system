# =========================================================
# SMART CAMPUS INFORMATION SYSTEM
# =========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# LAB 1 : STUDENT REGISTRATION & GRADE EVALUATION
# =========================================================

def student_registration():
    print("\n===== STUDENT REGISTRATION =====")
    student_id = input("Enter Student ID : ")
    name = input("Enter Student Name : ")
    marks = float(input("Enter Marks : "))
    if marks >= 90: grade = "A"
    elif marks >= 75: grade = "B"
    elif marks >= 60: grade = "C"
    elif marks >= 40: grade = "D"
    else: grade = "F"
    print("\n===== STUDENT DETAILS =====")
    print("Student ID :", student_id)
    print("Student Name :", name)
    print("Marks :", marks)
    print("Grade :", grade)
    with open("student_records.txt", "a") as file:
        file.write(f"{student_id},{name},{marks}\n")
    print("\nStudent Record Saved Successfully!")

# =========================================================
# LAB 2 : COURSE ENROLLMENT MANAGEMENT
# =========================================================

def course_enrollment():
    print("\n===== COURSE ENROLLMENT =====")
    courses = []
    max_courses = 5
    while True:
        if len(courses) >= max_courses:
            print("Maximum Course Limit Reached!")
            break
        course = input("Enter Course Name (or done): ")
        if course.lower() == "done": break
        credits = input("Enter Credits : ")
        if not credits.isdigit():
            print("Invalid Credits!")
            continue
        courses.append((course, int(credits)))
    print("\n===== ENROLLED COURSES =====")
    for c, cr in courses:
        print("Course :", c, "| Credits :", cr)
    print("Total Courses :", len(courses))

# =========================================================
# LAB 3 : STUDENT RECORD MANAGEMENT
# =========================================================

def student_records():
    print("\n===== STUDENT RECORD MANAGEMENT =====")
    students=[{"Name":"Arjun","Age":20,"Marks":85},{"Name":"Meera","Age":19,"Marks":92},{"Name":"Ravi","Age":21,"Marks":76}]
    for s in students:
        print("\nName :", s["Name"])
        print("Age :", s["Age"])
        print("Marks :", s["Marks"])
    # SET OPERATIONS
    event_A={"Arjun","Meera","Ravi"}
    event_B={"Meera","Anita"}
    print("\nCommon Participants :", event_A & event_B)
    print("All Participants :", event_A | event_B)
    print("Only Event A :", event_A - event_B)

# =========================================================
# LAB 4 : SEARCHING & SORTING (BUBBLE + LINEAR SEARCH)
# =========================================================

def search_sort_students():
    print("\n===== SEARCH & SORT STUDENTS =====")
    student_ids=[105,102,110,108,101]
    print("Original IDs :", student_ids)
    # BUBBLE SORT
    n=len(student_ids)
    for i in range(n):
        for j in range(0,n-i-1):
            if student_ids[j]>student_ids[j+1]:
                student_ids[j],student_ids[j+1]=student_ids[j+1],student_ids[j]
    print("Sorted IDs :", student_ids)
    # LINEAR SEARCH WITH POSITION
    target=int(input("Enter ID to Search : "))
    for i in range(len(student_ids)):
        if student_ids[i]==target:
            print("Student ID Found!")
            print("Position (Index) :", i)
            print("Position (Human readable) :", i+1)
            break
    else:
        print("Student ID Not Found!")

# =========================================================
# LAB 5 : FEE CALCULATION USING FUNCTIONS
# =========================================================

def calculate_fee(tuition,hostel=0,transport=0):
    return tuition+hostel+transport

def fee_calculation():
    print("\n===== FEE CALCULATION =====")
    tuition=float(input("Enter Tuition Fee : "))
    hostel=float(input("Enter Hostel Fee : "))
    transport=float(input("Enter Transport Fee : "))
    print("Total Fee :",calculate_fee(tuition,hostel,transport))

# =========================================================
# LAB 6 : FILE HANDLING
# =========================================================

def file_manager():
    print("\n===== FILE MANAGER =====")
    try:
        with open("student_records.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No Records Found!")

# =========================================================
# LAB 7 : DIRECTORY SCANNING
# =========================================================

def directory_scanner():
    print("\n===== DIRECTORY SCANNER =====")
    path=input("Enter Directory Path : ")
    try:
        if not os.path.exists(path):
            print("Invalid Path!")
            return
        items=os.listdir(path)
        if len(items)==0:
            print("Directory is Empty!")
        else:
            for item in items:
                print(item)
    except Exception as e:
        print("Error :",e)

# =========================================================
# LAB 8 : PERFORMANCE ANALYTICS
# =========================================================

def performance_analytics():
    print("\n===== PERFORMANCE ANALYTICS =====")
    try:
        df=pd.read_csv("student_performance.csv")
        print(df)
        print(df.describe())
        scores=df[["Math","Science","English"]].to_numpy()
        mean_scores=np.mean(scores,axis=0)
        print("Mean Scores :",mean_scores)
        plt.bar(["Math","Science","English"],mean_scores)
        plt.title("Average Subject Performance")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.show()
    except FileNotFoundError:
        print("student_performance.csv File Not Found!")

# =========================================================
# MAIN MENU
# =========================================================

while True:
    print("\n======================================")
    print(" SMART CAMPUS INFORMATION SYSTEM ")
    print("======================================")
    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Student Records")
    print("4. Search & Sort Students")
    print("5. Fee Calculation")
    print("6. File Manager")
    print("7. Directory Scanner")
    print("8. Performance Analytics")
    print("9. Exit")
    choice=input("Enter Choice : ")
    if choice=="1":student_registration()
    elif choice=="2":course_enrollment()
    elif choice=="3":student_records()
    elif choice=="4":search_sort_students()
    elif choice=="5":fee_calculation()
    elif choice=="6":file_manager()
    elif choice=="7":directory_scanner()
    elif choice=="8":performance_analytics()
    elif choice=="9":
        print("Exiting System...")
        break
    else:
        print("Invalid Choice!")