s=input("Enter the string:")
rev=''
original=s

for i in range(len(s)-1, -1, -1):
    rev+=s[i]    #reverses the string using negative indexing

    if rev==original:
        print(f"{original} is a palindrome")

# doubt: what if i want to check that a whole sentence is a palindrome or not.