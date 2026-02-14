s=input("Enter string:")
clear=''
for i in s:
    if i.isalnum() or i==" ":
        clear+=i
print("without punctuations:", clear)