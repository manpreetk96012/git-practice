s=input('Enter string:')
#step1: remove punctuation
clean=""

for ch in s:
    if ch.isalnum() or ch==" ":
        clean+=ch
#step2: lower case
clean=clean.lower()
#step3: split into words
words= clean.split()
#step4: count frequency
freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

print("word frequency:")
for word in freq:
    print(word, ":", freq[word])
