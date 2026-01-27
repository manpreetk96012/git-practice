n=int((input("")))
digit_sum=0
while n>0:
    digit=n%10
    digit_sum=digit_sum+digit
    n=n//10
print(f"{digit_sum} is the sum of digits")
