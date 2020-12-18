introString = input("enter your introduction: ")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        wordCount = wordCount+1
        characterCount = characterCount-1
if(wordCount<5):
    print("invalid intro")
print("no. of words in the string: ")
print(wordCount)
print("no. of letters in the string: ")
print(characterCount)