import string

f=open('two_cities_ascii.txt','r')
text=f.read()

Low_text=text.lower()

#remove punctuation marks
final_text= Low_text.translate(str.maketrans('', '', string.punctuation))

#split the words of the text
words=final_text.split()

#finding the most common object of a list
def most_common(lst,k):
    common=max(set(lst), key=lst.count)
    print(k,common)
    #deleting the most common so i can find the next
    j=0
    while j<len(lst):
        if lst[j]==common:
            lst.remove(common)
        j=j+1

#find the 10 most common words
print('Οι 10 πιο συχνές λέξεις είναι:')
words_copy=words
for i in range (1,11):
    most_common(words_copy,i)

#find the 3 most common 2 first characters
print('')
print('Οι πιο συχνεί συνδιασμοί των 2 πρώτων γραμμάτων είναι:')
#finding the first 2 chatacters of each word
first2_chars=[x[:2] for x in words]
for i in range (1,4):
    most_common(first2_chars,i)

#find the 3 most common 3 first characters
print('')
print('Οι πιο συχνεί συνδιασμοί των 3 πρώτων γραμμάτων είναι:')
#finding the first 3 chatacters of each word
first3_chars=[x[:3] for x in words]
for i in range (1,4):
    most_common(first3_chars,i)

f.close()