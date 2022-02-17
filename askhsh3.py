import string

f=open('two_cities_ascii.txt','r')
text=f.read()

#remove punctuation marks
final_text= text.translate(str.maketrans('', '', string.punctuation))

#split the words of the text
words=final_text.split()

#remove the words that their sum is 20
for i in range(0,(len(words))):
    for j in range(0,(len(words))):
        if i!=j:
            if len(words[i])+ len(words[j])==20:
                words[i]=''
                words[j]=''

#remove the epmpty objects
while(words.count('')):
    words.remove('')

#count the words characters 
words_length=[]
for x in range(0,len(words)):
    words_length.append(len(words[x]))

#prints the words and the characters of each
print('Υπάρχουν:')
for i in range(1,20):
    if words_length.count(i)!=0:
        print(words_length.count(i),'λέξεις',i,'γραμμάτων')
f.close()