
## Total of numbers from 1 to N 
#gaws
# num=int(input("Enter a number : "))
# Total=(num*(num+1))/2
# print (int(Total))

# for loop
# num=int(input("Enter a number : "))

# for i in range(0,num,1):
#    num=num+i

# print(num)   

##############################################################
#the biggest number between 3 numbers

# def biggest():
#  while True:   
#    numOne=int(input("Enter  number 1 : "))
#    numTwo=int(input("Enter  number 2 : "))
#    numThree=int(input("Enter  number  3 : "))
#    if numOne>numTwo:
#       if numOne>numThree:
#          print("number one is the biggest")
#       else:
#          print("number three is the biggest")
#    else:
#       if numTwo>numThree:
#          print("number two is the biggest")
#       else:
#          print("number three is the biggest")
#    repeat=input("do you want to repeat ? (y/n)")
#    if repeat!="y":
#     print("Thank you for using our app")
#     break      

# biggest()         

##############################################################
#triangle
# space=5
# for i in range(1,10,2):
  
#   print(' '*space,"*"*i)
#   space=space-1

  ##############################################################

#password check
# realPassword="123"
# attemps=3
# while attemps!=0:
#     print(f"You have {attemps} attemps")
#     password=input("Enter password : ")
#     if password==realPassword:
#         print("Welcome")
#         break
#     else:
#         print("Wrong")
#         attemps=attemps-1
# if attemps==0:
#     print("  maximum  attemps reached !")

##############################################################

#reverse a number
# number=input("Enter a number : ")
# print(number[::-1])

##############################################################

#prime numbers

# number=100
# prime=[]
# for number in range(number,0,-1):
#     loop=number-1
#     check=loop
#     for loop in range(loop,0,-1):
#         if number%loop==0:
#             break
  
#     if loop==1:    
#        prime.append(number) 

# print(prime)

##############################################################
s