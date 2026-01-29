n=int(input())
count=0

if n==0:
    count=1
else:
    while n>0:
        count=count+1
        n=n//10
print(f"{count} is the number of digits")