n = int(input())
if n%2!=0:
    print("its an odd-number so no even-number sum is calculated")

even_sum=0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    n=n//10

print(f"{even_sum} is the sum of even digit number")
    