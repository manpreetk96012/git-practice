s=input("")
consonants=0

for i in s:
    if i.isalpha() and i not in 'aeiouAEIOU':
        consonants+=1

print(consonants)

digit=0
for i in s:
    if i.isdigit():
        digit+=1
print(digit)
