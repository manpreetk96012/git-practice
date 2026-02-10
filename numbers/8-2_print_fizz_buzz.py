for i in range(1, 101, 1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

# for good presentation using columns use:
# print(f"{'fizzbuzz':10}", end=" ")