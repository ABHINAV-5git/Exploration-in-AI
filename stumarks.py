#Student Marks, Percentage and Grade
name = input("Enter  your student name:")
n = int(input("Enter number of subjects:"))
total = 0
for i in range(1,n+1):
     mark = float(input("Enter mark for subject {i}:"))
     total+=mark
     percentage = total/n
if percentage>=90:
     grade = "A+"
     perfomance = "outstanding performance"
elif percentage>=80:
     grade = "A"
     perfomance = "Excellent performance"
elif percentage >= 70:
     grade = "B"
     perfomance = "very good performance"
elif percentage  >= 60 :
     grade = "C"
     perfomance = "Good performance"
elif percentage >= 50  :
     grade =  "D"
     perfomancce="Average Performance3"
else:
     grade = "E"
     perfomance = "Very bad try to improve"

print("Student name is :",name)
print("Number of subjects:",n)
print("Percentage:",percentage)
print("Grade is",grade)
print("Perfomance:",perfomance)