import numpy as np

students = np.array([
    "Aman", "Riya", "Rahul",
    "Priya", "Neha", "Arjun"
])

maths = np.array([78, 92, 65, 88, 95, 81])

science = np.array([82, 90, 70, 91, 89, 84])

english = np.array([80, 85, 75, 94, 90, 79])

attendance = np.array([92, 88, 75, 96, 99, 85])

# Basic Information

print("Students:")
print(students)

print("\nMaths Marks:")
print(maths)

print("\nScience Marks:")
print(science)

print("\nEnglish Marks:")
print(english)

print("\nAttendance:")
print(attendance)

print("\nTotal Number of Students:")
print(students.size)

# Total & Average

total_marks = maths + science + english
print("\nTotal Marks:")
print(total_marks)

average_marks = total_marks / 3
print("\nAverage Marks of Each Student:")
print(average_marks)

total_students_marks = np.sum(total_marks)
print("\nTotal Students Marks:")
print(total_students_marks)

average_students_marks = np.mean(total_marks)
print("\nClass Average:")
print(average_students_marks)

highest_total_marks = np.max(total_marks)
print("\nHighest Total Marks:")
print(highest_total_marks)

lowest_total_marks = np.min(total_marks)
print("\nLowest Total Marks:")
print(lowest_total_marks)

median_total_marks = np.median(total_marks)
print("\nMedian Total Marks:")
print(median_total_marks)

variance_total_marks = np.var(total_marks)
print("\nVariance of Total Marks:")
print(variance_total_marks)

standard_deviation_total_marks = np.std(total_marks)
print("\nStandard Deviation of Total Marks:")
print(standard_deviation_total_marks)

# Subject Analysis

print("\nHighest Maths Marks:")
print(np.max(maths))

print("\nLowest Maths Marks:")
print(np.min(maths))

print("\nAverage Maths Marks:")
print(np.mean(maths))

print("\nHighest Science Marks:")
print(np.max(science))

print("\nLowest Science Marks:")
print(np.min(science))

print("\nAverage Science Marks:")
print(np.mean(science))

print("\nHighest English Marks:")
print(np.max(english))

print("\nLowest English Marks:")
print(np.min(english))

print("\nAverage English Marks:")
print(np.mean(english))

# Attendance Analysis

highest_attendance = np.max(attendance)
print("\nHighest Attendance:")
print(highest_attendance)

lowest_attendance = np.min(attendance)
print("\nLowest Attendance:")
print(lowest_attendance)

average_attendance = np.mean(attendance)
print("\nAverage Attendance:")
print(average_attendance)

student_highest_attendance = students[np.argmax(attendance)]
print("\nStudent with Highest Attendance:")
print(student_highest_attendance)

student_lowest_attendance = students[np.argmin(attendance)]
print("\nStudent with Lowest Attendance:")
print(student_lowest_attendance)

# Topper Analysis

topper = students[np.argmax(total_marks)]
print("\nTopper:")
print(topper)

lowest_scorer = students[np.argmin(total_marks)]
print("\nLowest Scorer:")
print(lowest_scorer)

students_above_250 = students[total_marks > 250]
print("\nStudents Scoring Above 250:")
print(students_above_250)

students_below_230 = students[total_marks < 230]
print("\nStudents Scoring Below 230:")
print(students_below_230)

# Filtering

attendance_above_90 = students[attendance > 90]
print("\nAttendance Above 90%:")
print(attendance_above_90)

attendance_below_80 = students[attendance < 80]
print("\nAttendance Below 80%:")
print(attendance_below_80)

maths_above_90 = students[maths > 90]
print("\nStudents Above 90 in Maths:")
print(maths_above_90)

science_above_90 = students[science > 90]
print("\nStudents Above 90 in Science:")
print(science_above_90)

english_above_90 = students[english > 90]
print("\nStudents Above 90 in English:")
print(english_above_90)

# Sorting

ascending_total_marks = np.sort(total_marks)
print("\nTotal Marks in Ascending Order:")
print(ascending_total_marks)

descending_total_marks = np.sort(total_marks)[::-1]
print("\nTotal Marks in Descending Order:")
print(descending_total_marks)

ascending_attendance = np.sort(attendance)
print("\nAttendance in Ascending Order:")
print(ascending_attendance)

descending_attendance = np.sort(attendance)[::-1]
print("\nAttendance in Descending Order:")
print(descending_attendance)

# Searching

position_of_priya = np.where(students == "Priya")
print("\nPosition of Priya:")
print(position_of_priya)

student_maths_95 = students[np.where(maths == 95)]
print("\nStudent Scoring 95 in Maths:")
print(student_maths_95)

student_attendance_99 = students[np.where(attendance == 99)]
print("\nStudent with 99% Attendance:")
print(student_attendance_99)

# Rank Analysis

sorted_indices = np.argsort(total_marks)

print("\nRank Indices:")
print(sorted_indices)

best_student = students[sorted_indices[-1]]
print("\nBest Student:")
print(best_student)

second_best_student = students[sorted_indices[-2]]
print("\nSecond Best Student:")
print(second_best_student)

worst_student = students[sorted_indices[0]]
print("\nWorst Student:")
print(worst_student)

# Final Report

print("\n========== Smart Student Dashboard ==========")

print("Total Students:", students.size)

print("Class Average:", average_students_marks)

print("Highest Total:", highest_total_marks)

print("Lowest Total:", lowest_total_marks)

print("\nTopper:", topper)

print("Lowest Scorer:", lowest_scorer)

print("\nHighest Attendance:", highest_attendance)

print("Lowest Attendance:", lowest_attendance)

print("\nStudents Above 250:")
print(students_above_250)

print("\nStudents Below 230:")
print(students_below_230)

print("\nBest Student:", best_student)

print("Second Best Student:", second_best_student)

print("Worst Student:", worst_student)

print("\n=============================================")