#Avery, error handling calculator


# Function to perform the chosen operation
def perform_operation(num1, num2, operation):
   # Check the operation and calculate the result
   if operation == 'add':
       return num1 + num2
   elif operation == 'subtract':
       return num1 - num2
   elif operation == 'multiply':
       return num1 * num2
   elif operation == 'divide':
       if num2 == 0:
           return "Error: Cannot divide by 0."
       else:
           return num1 / num2
   else:
       return "Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."


# Main program loop
while True:
   try:
       # Get user input for two numbers and the operation
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
      
       # Get the operation
       operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()


       # Perform the operation and print the result
       result = perform_operation(num1, num2, operation)
       print(f"The result of {operation}ing {num1} and {num2} is: {result}")
      
       # Ask the user if they want to continue
       continue_program = input("Do you want to perform another calculation? (yes/no): ").lower()
       if continue_program != 'yes':
           break
  
   except ValueError:
       print("Error: Please enter valid numbers.")
