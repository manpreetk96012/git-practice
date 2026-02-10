s=input("Enter a string: ")
clean="" 
for ch in s:
    if ch.isalnum():
        clean+=ch.lower()

rev=clean[::-1]
if clean==rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")