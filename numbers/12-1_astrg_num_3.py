n=int(input())
amstrg_sum=0
original=n

while n>0:
    digit=n%10
    amstrg_sum+=digit**3
    n//=10

if amstrg_sum==original:
    print(f"{original} is an armstrong number as sum of it's cubes is {amstrg_sum}.")
else:
    print("not an armstrong number")
