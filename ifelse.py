light = "red"

if(light== "red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
     print("look")

age = 25

if(age>=18):
    print("can vote")
else:
    print("can not vote")

    #odd or even 
num = int(input("enter number:"))

if(num%2 ==0):
    print("even")
else:
    print("odd")

    #largest numbers
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print("second number is largset",b)
else:
    print("third is largest",c);
