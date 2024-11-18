#Avery, what is my grade


# Dictionary to store class names and corresponding letter grades
grades = {}


# Loop to input multiple classes and their grade percentages
while True:
   # Get class name and grade percentage
   class_name = input("Enter the class name (or 'done' to finish): ")
  
   if class_name.lower() == 'done':
       break


   try:
       grade_percentage = float(input(f"Enter your grade percentage for {class_name}: "))
      
       # Determine letter grade based on the grade percentage
       if grade_percentage >= 90:
           letter_grade = 'A'
       elif grade_percentage >= 80:
           letter_grade = 'B'
       elif grade_percentage >= 70:
           letter_grade = 'C'
       elif grade_percentage >= 60:
           letter_grade = 'D'
       else:
           letter_grade = 'F'
      
       # Store class and letter grade
       grades[class_name] = letter_grade
  
   except ValueError:
       print("Invalid input! Please enter a valid percentage.")


# After user finishes entering all grades, print all class names and letter grades
print("\nClass Names and Corresponding Letter Grades:")
for class_name, letter_grade in grades.items():
   print(f"{class_name}: {letter_grade}")
