import json
from urllib.request import FancyURLopener, Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=json.loads(data)
#finding the last rounds number
rounds=data["round"]

#finding the last random number
numbers=[data["randomness"]]

#finding the last random number
for i in range (1,100):
    rounds=rounds-1
    req = Request("https://drand.cloudflare.com/public/{}".format(rounds), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data=json.loads(data)
    numbers.append(data["randomness"])

#converting the hex numbers in binary
final_num=''
for i in range (0,100):
    s = bin(int(numbers[i], 16))
    final_num+=s


#finding the biggest unbreakable sequence of 0 or 1
def find_max(n):
    if n=='0':
        j='1'
    else:
        j='0'
    #removing the characters that are not 1 or 0
    num=final_num.replace('0b','')
    num=num.replace(']','')
    num=num.replace('[','')
    #replacing the number that breakes the sequences with space character  
    num=num.replace(j,' ')
    x=num.split()
    #returning the max sequence
    return max(x, key=len)

print('Η μεγαλήτερη ακολουθία απο συνεχόμενα "0" είναι:')
print(find_max('0'))

print('Η μεγαλήτερη ακολουθία απο συνεχόμενα "1" είναι:')
print(find_max('1'))
