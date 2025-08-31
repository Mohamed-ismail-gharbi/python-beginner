#area of rectangle
while True:
 length=int(input('Enter length : '))
 width=int(input('Enter width : '))
 if width<length:
  print(f"area is : {width*length}")
 else:
     print('width shouldn\'t be bigger then length') 
 repeat=input("do you want to repeate ? (y/n) : ")
 if repeat!="y":
  break