#avery shopping list


shopping_list = []


#Function to add an item to the list
def add():
  item = input("Enter an item to add: ")
  shopping_list.append(item)
  print(f"Added '{item}' to the shopping list.")
  print_list()  #this is the end of the add() function


#function to remove an item from the list
  def remove():
      item = input("Enter an item to remove: ")
      if item in shopping_list:
          shopping_list.remove(item)
          print(f"Remove '{item}' is not in the shopping list.")
      else:
          print(f"'{item}' is not in the shopping list.")
          print_list()  #this is the end of the remove() function


#function to print the current list
def print_list():
          if shopping_list:
               print("Current Shopping List:", shopping_list)
          else:
               print("Your shopping list is empty.")  #end of print_list()


#main loop
          while True:
              action = input("""
                             What would you like to do?


                             Enter 1 to add an item
                             Enter 2 to remove an item
                             Enter 3 to leave the list:
                            
                             """)
             
              if action == "1":
                  add()
              elif action == "2":
                  remove()
              elif action == "3":
                  print("Have a nice day!")
                  break
              else:
                  print("Invalid input, please try again.")