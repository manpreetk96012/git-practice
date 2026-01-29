n=int(input())
original=n
palin=0
while n>0:
    drome=n%10
    palin=palin*10+drome
    n=n//10

if original==palin:
        print(f"{original} is a palindrome")
        
else:
    print("not a palindrome")
