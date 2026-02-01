s=input("enter the string:")
vowel=0
consonant=0
digit=0
special=0

for i in s:
    if i.isalpha():     #counts only alphabets
        if i in 'aeiouAEIOU':
            vowel+=1
        else:
            consonant+=1
        
    if i.isdigit():     #counts only digits
        digit+=1
    #counts special character + spaces
    elif not i.isalnum():      #counts number + alphabets only
        special+=1
        
        
print(f"vowel count:{vowel}")
print(f"consonant count:{consonant}")
print(f"special count:{special}")
print(f"digit count:{digit}")