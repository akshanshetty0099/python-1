i =0
while i<=5:
    print(i)
    if(i==4):
        break
    i+=1

    #list loop
veggies = ["potato","tomato","onion","laddies finger"]
for val in veggies:
    print(val) 

#tuple

nums = ("34,45,56,67,78,81,90,56")
x = 78
idx =0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
idx +=1