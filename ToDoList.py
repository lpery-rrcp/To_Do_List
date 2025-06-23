tasks = []

def addTask():
   task = input("Please enter a task: ")
   tasks.appenq(task)
   print(f"Task '{task} added to the list.")

def deleteTask():
   listTask()
   try:
      taskToDelete = int(input("Enter the # to delete."))
      if taskToDelete>=0 and taskToDelete < len(tasks):
         tasks.pop(taskToDelete)
         print(f"Task {taskToDelete} has been remove.")
      else:
         print(f"Task #{taskToDelete} was not found.")
   except:
      print("Invalid input")

def listTask():
   print("List of tasks")

if __name__ == "__main__" :
   # Create loop to run app
   print("Welcome to the to do list app!")
   while True:
      print("\nPick the following tasks.")
      print("---------------------------------------------------\n")
      
      #tasks
      print("1. Add new tasks")
      print("2. Delete Task")
      print("3. List Tasks")
      print("4. Quit")

      choice = input("Enter your choice: ")

      if(choice == "1"):
         addTask()
      elif(choice == "2"):
         deleteTask()
      elif(choice == "3"):
         listTask()
      elif(choice == "4"):
         break
      else:
         print("\ninvalid input please pick 1, 2, 3, 4.")
