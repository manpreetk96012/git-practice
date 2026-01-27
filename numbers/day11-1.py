n=int(input())
perfect_sum=0
original=n
while n>0:
    for i in range(1, n):
        
        if n%i==0:
            perfect_sum=perfect_sum+i
    n=n//10
if perfect_sum==original:
     print(f"{perfect_sum} is a perfect number.")
else:
    print(f"{original} is not a perfect number.")