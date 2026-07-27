#create a console based Expense tracker ,That allows the user to record the  daily expenses and view summeries like total spending.

expenseslist=[]  #List of expeses in form of dictionary
print("Wellcome to expense Tracker: ")

while True :
    print("\n====Menu===")
    print("1.add expenses ")
    print("2.View all expense")
    print("3.view total spending")
    print("4.Exit")
    
    
    
    choice=input("please enter your choice:")
    
    
    #1.Add EXPENSE
    if (choice =="1") :
        date=input("Enter the date:")
        category=input("Enter the category(food,cloth,makeup,books):")
        description=input("Give more detail:")
        amount=float(input("Enter the amount:"))
        
        
        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        
        expenseslist.append(expense)
        print("\n DONE BRO. Expenses added succesfully")
        
        
   #2.VIEW ALL EXPENSES 
    elif(choice=="2"):
       if(len(expenseslist))==0:
         print("NO Expenses added .Jao pehele kharcha karo.")
       else:
         print("====Ye he apka sar aexpenses===")
         count=1
       for eachkharcha in expenseslist:
        print(f"kharchanumber {count}->{eachkharcha['date']},{eachkharcha['category']},{eachkharcha['description']},{eachkharcha['amount']}")
       count=count+1
           
    #3.VIEW TOTAL SPENDING
    elif(choice=="3"):
      total=0
      for eachkharcha in expenseslist:
        total=total + eachkharcha["amount"]
      print("\n TOTAL KHARCHA =",total)
                
        
   #4.EXIT           
    elif choice == "4":
      print("Thank you for using this system")
      break
    else:
     print("INVALID CHOICE, TRY AGAIN")
    
    
    
    