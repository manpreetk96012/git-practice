n=int(input(""))
rev_number=0
while n>0:
    number=n%10
    rev_number=rev_number*10+number
    n=n//10
print(f"{rev_number} is the reversed number")