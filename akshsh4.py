import random
card=[i for i in range(1,11)]
suit=["C","S","H","D"]
figure=["J","Q","K"]
card=card+figure

DECK=[]
for i in suit:
	for j in card:
		DECK.append([i,j])
random.shuffle(DECK)
j=0
def get_card_value(c):
	if c[1] in figure:
		return 10
	else:
		return c[1]
def sum_cards(LST):
	score=0
	for c in LST:
		score+=get_card_value(c)
	return score

player1=0
player2=0
draw=0
#give cards
for i in range(0,100):
	comp_cards=[DECK[0],DECK[1],DECK[2]]
	my_cards=[DECK[3],DECK[4],DECK[5]]
	comp_score=sum_cards(comp_cards)
	my_score=sum_cards(my_cards)

#finding the outcome of the game 
	if my_score>comp_score:
		player1=player1+1
	elif comp_score>my_score:
		player2=player2+1
	else:
		draw=draw+1

	random.shuffle(DECK)
print('Στα 100 παιχνίδια:')
print('Ο πρώρος παίκτης κέρδισε:',player1,'φορές')
print('Ο δεύτερος παίκτης κέρδισε:',player2,'φορές')
print('Ήρθε ισοπάλια:',draw,'φορές')
print('')

player1=0
player2=0
draw=0	
def new_func():
    return print

for i in range(0,100):
	flag=False
	j=0
	while flag==False:
		#making sure that the first cards value is going to be 10
		if DECK[j][1]==10:
			comp_cards=[DECK[j],DECK[j+1],DECK[j+2]]
			flag=True
		elif DECK[j][1]=='J':
			comp_cards=[DECK[j],DECK[j+1],DECK[j+2]]
			flag=True
		elif DECK[j][1]=='Q':
			comp_cards=[DECK[j],DECK[j+1],DECK[j+2]]
			flag=True
		elif DECK[j][1]=='K':
			comp_cards=[DECK[j],DECK[j+1],DECK[j+2]]
			flag=True
		j+=1
	my_cards=[DECK[j],DECK[j+1],DECK[j+2]]
	comp_score=sum_cards(comp_cards)
	my_score=sum_cards(my_cards)


	if my_score>comp_score:
		player1=player1+1
	elif comp_score>my_score:
		player2=player2+1
	else:
		draw=draw+1
	
	random.shuffle(DECK)
print('!!ΝΕΟ!!')
print('Στα 100 παιχνίδια:')
print('Ο πρώρος παίκτης κέρδισε:',player1,'φορές')
print('Ο δεύτερος παίκτης κέρδισε:',player2,'φορές')
print('Ήρθε ισοπάλια:',draw,'φορές')
