while True:
 numOne=int(input("Enter number one : "))
 numTwo=int(input("Enter number two : "))

 print(f"sum : {numOne+numTwo}")
 print(f"sub : {numOne-numTwo}")
 print(f"multiplication : {numOne*numTwo}")
 if numTwo != 0:
  print(f"devision : {numOne/numTwo}")
 else:
     print("Number Two is zero ") 
 again=input("do you want to repeat ?(y/n) : ").strip().lower()
 if again!="y":
  print ("Thank you for use our app ! ")
  break