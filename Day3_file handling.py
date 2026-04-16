task=[]
try:
    with open ("/Users/kavi/Desktop/fileprac.txt") as f:
      for line in f:
           task.append(line.strip())
except FileNotFoundError:
     pass
     

def save_task():
       with open ("/Users/kavi/Desktop/fileprac.txt","w") as f:
            for i in task:
                 f.write(i+"\n")          
           
while True:
  print("\n1.Add task")
  print("2.View task")
  print("3.Remove task")
  print("4.Exit")

  try:
        select = int(input("Enter the choice: "))
  except ValueError:
        print("Please enter a valid number")
        continue
  

  match select:
       case 1: 
            new_task=input("Enter the new task")
            task.append(new_task)
            save_task()
            print("Task added")
       case 2:
            if len(task) == 0:
                print("No tasks to show")
            else:
                for i in range(len(task)):
                    print(i+1,".",task[i])
       case 3:
            if len(task)==0:
                 print("Invalid")
            else:
                num=int(input("Enter task number to be removed"))
                if 0<num<=len(task):
                    remove= task.pop(num-1)
                    save_task()
                    print("Task removed successfully",remove)
                
       case 4:
                print("Exit")
                break
       case _:
                print("Invalid")
   
  


        









