def reverseWords(input):
    inputWords = input.split(" ") 
    inputWords=inputWords[-1::-1] 
    output = ' '.join(inputWords) 
    return output 
input = 'BMSCE COLLEGE OF ENGINEERING'
rev=reverseWords(input)
words=rev.split(" ")
newWords = [word[::-1] for word in words]
reverse = " ".join(newWords)  
print(rev)
print(reverse)

