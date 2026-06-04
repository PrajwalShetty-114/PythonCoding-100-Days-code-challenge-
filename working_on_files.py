import files


with open('sample.txt','r+') as file:
    data=file.read()
    list_of_words=data.split()

# print(list_of_words)
for word in list_of_words:
    print(word)
    
   

