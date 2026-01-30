s=input("")
vowels=0

for i in s:     #loop range: whatever is input becomes the range itself
    #loop through each character in the string
    if i in  'aeiouAEIOU':      #check if the character is a vowel
        vowels+=1       #counts vowels
print(vowels)
    
    