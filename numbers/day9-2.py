n=int(input())
count=0

while n>0:
    digit=n%10
    count=count+1
    n=n//10

if count==3:
        print("it's a 3 digit number")
else:
        print("it's not a 3 digit number")