#when multiple spaces, leading ot trailing spaces exists

s=input("Enter the string:")
word=s.split()

print(f"word count:{len(word)}")

#using loops

s=input("Enter the string:")
word=0

for i in s:
    if i==' ':
        word+=1

print(f"word count:{word+1}")

#using indexing

s=input("Enter the string:")
word=0

for i in range(len(s)):
    if s[i]==' ':
        word+=1

print(f"word count:{word+1}")


