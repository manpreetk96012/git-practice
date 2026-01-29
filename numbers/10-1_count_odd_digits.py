n=int(input())
odd_count=0


while n>0:
    digit=n%10

    if (digit%2)==0:
        print()
        
    elif (digit%2)!=0:
        odd_count=odd_count+1
        
    n=n//10
print(f"number of odd digits are {odd_count}")
