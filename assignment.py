
students = {
   "STD001": {"name":"Emma", "score":85},
   "STD002": {"name":"Ada", "score":72},
   "STD003": {"name":"John", "score":60}
}

while True:
      print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
      print("1. View all students")
      print("2. Add a new student")
      print("3. Update a student's score")
      print("4. Delete a student")
      print("5. Search for a student")
      print("6. Display students who passed")
      print("7. Display student grades")
      print("8. Exit")

choice = input("Enter your choice: ")
#1. View all students
if choice == "1":
   for student_id, details in students.items():
      print(student_id, details["name"], details["score"])
      #or
      #print(f"{student_id}: {details['name']} - {details['score']}")
# 2. Add a new student      
elif choice == "2":
   student_id = input("Enter student ID:")
   # name = input("Enter student name:")
   # score = input("Enter student score:")

   if student_id in students:
      print("Student ID already exists.")
   else:
      name = input("Enter student name:")
      score = int(input("Enter student score:"))
      
      students.setdefault(
         student_id,
         {"name": name, "score": score}
      )
      
      print("Student added successfully.")
      
# 3. Update a student's score
elif choice == "3":
   student_id = input("Enter student ID.")
   student = students.get(student_id)
   
   if student is None:
      print("student not found.")
   else:
      new_score = int(input("Enter new score."))
      student.update({"score": new_score })
      print("Student's score updated successfully.")
      
# 4. Delete a student
elif choice == "4":
   student_id = input("Enter student ID to delete:")
   
   if student_id in students:
      students.pop(student_id)
      print("Student deleted successfully.")
   else:
      print("Student not found.")
      
# 5. Search for a student
elif choice == "5":
   student_id = input("Enter student ID to search:")
   student = students.get(student_id)
   
   if student is None:
      print("Student not found.")
   else:
      print(f"Name: {student['name']}")
      print(f"score: {student['score']}")
      
# 6. Display students who passed
elif choice == "6":
   passed_students = {
      student_id: details
      for student_id, details in students.items()
      if details["score"] >= 50
   }
   print("\nStudents who passed:")
   
   for student_id, details in passed_students.items():
      print(f"{student_id}: {details['name']} - {details['score']}")
      
# 7. Display student grades
elif choice == "7":
   grades = {
      student_id: "A" if details["score"] >= 70
      else "B" if details["score"] >= 60
      else "C" if details["score"] >= 50
      else "D" if details["score"] >= 40
      else "F"
      for student_id, details in students.items()
   }       
   
   print("\nStudents Grades:")

for student_id, grade in grades.items():
   print(f"{student_id}: {grade}")
   
# 8. Exit
elif choice == "8":
    print("Goodbye!")
    break

# Invalid choice
else:
    print("Invalid choice. Please try again.")      
      


#    A simpler and clearer way of using .setdefault():
# elif choice == "2":
# student_id = input("Enter student ID:")
   
# if student_id in students:
#       print("Student ID already exists.")
# # else:
#    name = input("Enter student name: ")
#    score = int(input("Enter student score: "))

#    students.setdefault(student_id, {
#       "name": name,
#       "score": score
# })

# print("Student added successfully.")
# elif choice == "3":
#    student_id = input("Enter student ID:")
#    student = students.get(student_id)
   
#    if student is None:
#       print("Student not found.")
#    else:
         