introstring = input("Enter your introduction : ")
print(introstring)
characterCount = 0
wordCount = 1
for i in introstring:
    characterCount = characterCount+1
    if(i == ' '):
        wordCount = wordCount+1
print("Number of words : ", wordCount)
print("Number of Characters : ", characterCount)