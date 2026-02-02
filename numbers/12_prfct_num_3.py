n=int(input())
prfct_sum=0
original=n

for i in range(1, n):
    
    if n%i==0:
        prfct_sum+=i

if original==prfct_sum:
    print(f"{original} is a perfect number")
else:
    print("not a perfect number")