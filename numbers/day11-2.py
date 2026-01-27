n=int(input())
amstrg_sum=0
original=n

while n>0:
    
    digit=n%10
    amstrg_sum=amstrg_sum+digit**3
    n=n//10

if amstrg_sum==original:
    print(f"{original} is an armstrong number.")
else:
    print("its not an armstrong number.")