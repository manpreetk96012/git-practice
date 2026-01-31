x=int(input())
y=int(input())
z=int(input())
if x==y==z:
    print("all numbers are equal")
elif x>=y and x>=z:
    print(f"{x} is largest")
elif y>=x and y>=z:
    print(f"{y} is the largest")
else:
    print(f"{z} is largest")