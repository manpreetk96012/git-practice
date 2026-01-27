n=int(input())
even_sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        even_sum=even_sum+digit
    n=n//10
print(f"sum of even digits is {even_sum}")
