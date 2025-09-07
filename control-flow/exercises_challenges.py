
# Elevator
# floors=int(input("Enter number of floor : "))
# defaultFloor=int(input("Enter default floor : "))
# if defaultFloor>floors:
#     for defaultFloor in range(defaultFloor,floors,-1):
#         time.sleep(1)
#         if defaultFloor==floors+1:
#             print(f"Elevator in {floors+1}")  
#             print("you are in the right floor")
#         else:    
#          print(f"Elevator in {defaultFloor}")

# else:
     
#        for defaultFloor in range(defaultFloor,floors,+1):
#         time.sleep(1) 
#         if defaultFloor==floors-1:
#             print(f"Elevator in {floors-1}")   
#             print("you are in the right floor")
#         else:    
#          print(f"Elevator in {defaultFloor}")         

##############################################################

#ATM
# balance=1000

# while True:
#     process=input("choose process : Deposit(d) Withdrawl(w) Account statement(s) : ").lower()
#     if process=="d":
#         depositAmount=int(input("Enter amount : "))
#         balance=balance+depositAmount
#     elif process=="w":
#         withdrawlAmount=int(input("Enter amount : "))
#         balance=balance-withdrawlAmount  
#     elif process=="s":
#         print(f"Your balance is : {balance}")    
#     else:
#         print("invalaid choose") 
          
#     repeat=input("do you want to repeat ? (y/n)")
#     if repeat!="y":
#      print("Thank you for using our app")
#      break               
##############################################################
#to do
# ToDo=['orange','apple','banana']

# while True:
#     choose=input("do you want to show list(s) or add an item(a) or remove an item(r) : ").lower()     
#     if choose=='s':
#         for index, value in enumerate(ToDo):
#          print(f'Your list is : {index+1} {value}')
#     elif choose=='a':  
#       item=input('Enter an item : ')
#       if item=="":
#          print("invalaid")   
#       else:   
#        ToDo.append(item)    
#     elif choose=="r":
#         for index, value in enumerate(ToDo):
#          print(f'Your list is : {index+1} {value}')
#         itemToRemove=int(input("Enter item number : "))
#         if itemToRemove>len(ToDo)or itemToRemove<1:
#             print("invalaid")   
#         else:    
#          for index, value in enumerate(ToDo):
#             if index+1==itemToRemove:
#                 ToDo.pop(index)
#     else:
#         print("invalaid")         
#     repeat=input("do you want to repeat ? (y/n)")
#     if repeat!="y":
#       print("Thank you for using our app")
#       break    

##############################################################



