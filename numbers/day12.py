n=int(input())
prfct_sum=0

for i in range(1, n):
    
    if n%i==0:
        prfct_sum+=i
        print(f'{prfct_sum} is a perfect number')
    else:
        print("not a perfect number")