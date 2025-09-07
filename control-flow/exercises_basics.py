
#exrecices 
##############################################################
# multiplication table
# for i in range(10):
#     for j in range(10):
#         print(f"{i} * {j} = {i*j}")
#     print("##############")

##############################################################
## guess the number game 
# while True:
#     num=random.randint(1,10000)  
#     while True:
#      userGuess= int(input("guess a number between 1 and 10000 : "))
#      if userGuess==num:
#         print("Right !")
#         break 
#      elif userGuess>10000:
#         print("you must choose a number less than 10000")
#      elif userGuess>num:
#         print("Wrong! the right number is less then your guess")
#      elif userGuess==888:
#         print(num)   
    
#      else:
   
#         print("Wrong! the right number is big then your guess")   
#     repeat=input("do you want to repeat ? (y/n)")
#     if repeat!="y":
#         break
# while True:
#  nums=int(input("Enter a number : "))
#  userChoose=input("Do you want even or odd numbers ? (e/o) : ").lower()
#  if userChoose=="e": 
#     for nums in range(nums,0,-1):   
#      if(nums%2==0):
#        print(f"-{nums}-")
#      else:
#       continue  
#  elif userChoose=="o":
#        for nums in range(nums,0,-1):  
#           if(nums%2!=0):
#            print(f"-{nums}-")
#           else:
#            continue    
#  else:
#      print("invalid choose")
#  repeat=input("do you want to repeat ? (y/n)")
#  if repeat!="y":
#     print("Thank you for using our app")
#     break 

##############################################################
#Timer
# num=int(input("Enter a number : "))

# while True:
#    print(num)
#    num=num-1
#    time.sleep(1)
#    if num==0:
#       print("Time ! ")
#       break

##############################################################
