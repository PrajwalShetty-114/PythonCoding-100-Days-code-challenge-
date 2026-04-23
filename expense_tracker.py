expenses={}
# global count
count=0
def show_options():
      print('''
            Enter 1 for Add Expenses
            Enter 2 for View Expenses
            Enter 3 for Show Total
            Enter 4 for Exit
            Enter 5 for whole dictionary
      ''')

def add_expenses(name,amount,category):
      global count
      if len(expenses)!=0:
            for Key in expenses.keys():
                  if name == expenses[Key]["name"]:
                        user_categories=expenses[Key]["categories"]
                        user_categories.setdefault(category,amount)
                        break
            else:
                  # global count
                  count+=1
                  key="user"+str(count)
                  expenses.setdefault(key,{})
                  user=expenses[key]
                  user.setdefault("name",name)
                  user.setdefault("categories",{})
                  categories=user["categories"]
                  categories.setdefault(category,amount)
                  
      else:
            # global count
            count=count+1
            key="user"+str(count)
            expenses.setdefault(key,{})
            user=expenses[key]
            user.setdefault("name",name)
            user.setdefault("categories",{})
            categories=user["categories"]
            categories.setdefault(category,amount)
      
show_options()
selected_num=int(input("Enter the correct number for the necessary action\n"))
# count=0
while selected_num!=4:
      # show_options()
      if selected_num==1:
            # count=count+1
            name=input("Enter your name :")
            amount=int(input("Enter the amount :"))
            category=input("What category did you spend the money? :")
            add_expenses(name,amount,category)
      elif selected_num==2:
            
            length=len(expenses)
            if length>0:
                  name=input("Enter your name :")
                  for user in expenses:
                        if expenses[user]["name"]==name:
                              print(expenses[user])
                              break
                  else:
                        print("No such user found")
            else:
                  print("Please enter the Users (User list is empty)")

      elif selected_num==3:
            length=len(expenses)
            if length>0:
                  name=input("Enter the name of the person you want to view the total expenses\n")
                  total=0
                  flag=True
                  for user in expenses:
                        if expenses[user]["name"]==name:
                              categories=expenses[user]["categories"]
                        
                              for Category in categories:
                                    total=total+categories[Category]
                              break      
                  else:
                        flag=False
                        print("No such user found")
                  if flag:
                        print(total)
            else:
                  print("The expense list is empty")
      elif selected_num==5 :
            for user in expenses: 
                  print(expenses[user])
                  print("\n")
      else:
            print("Choose a valid number")
      show_options()
      selected_num=int(input("\nEnter the correct number for the necessary action\n"))
      