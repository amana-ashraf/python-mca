line=input("Enter a line: ").lower().split()
occurence={}
for word in line:
    occurence[word]=occurence.get(word,0)+1
print(occurence)