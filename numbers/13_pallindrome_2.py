n=int(input())
palin=0     
original=n  

while n>0:
    drome=n%10     #to get last digit
    palin=palin*10+drome     #to get values of palin after iterations (mathmatically take note)
    n//=10       #to end loop
if palin==original:
    print(f"{original} is a pallindrome.")
else:
    print("its not a pallindrome.")