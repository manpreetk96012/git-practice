n=int(input())
palin=0
original=n

while n>0:
    drome=n%10
    palin=palin*10+drome
    n//=10
if palin==original:
    print(f"{original} is a pallindrome.")
else:
    print("its not a pallindrome.")