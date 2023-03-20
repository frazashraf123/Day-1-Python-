#Q.1- Program to check the given number is multiple of 3 or 5 or both 3 and 5 else print invalid    
num = int(input())
if(num%3==0 and num%5==0):
    print("multiple of 3 and 5")
elif(num%3==0):
    print("multiple of 3")
elif(num%5==0):
    print("multiple of 5")
else:
    print("invalid")
