# Question No. 1
total_marks = 0

for i in range(1, 6):
    marks = float(input("Enter marks of subject " + str(i) + ": "))
    total_marks = total_marks + marks

percentage = (total_marks / 500) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n-- Student Result --")
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Pass/Fail:", result)