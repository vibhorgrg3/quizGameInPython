"""
learn using apis and add questions on the go :D
"""

import data as d
import os
print(d.question_data[1]['answer'])

class player:
    name=''
    score=0

def displayQuestion(ind):
    print('Question ',ind+1,d.question_data[ind]['text'],'True or Fasle?')

def askQuestion(player,ind):
    displayQuestion(ind)
    ch=input('\nEnter answer: ')
    print(ch)
    if(ch.lower()==d.question_data[ind]['answer'].lower()):
        print('Correct')
        player.score+=1
    else:
        print('Wrong')
def gamePlay():
    p=player()
    for i in range(12):
        askQuestion(p,i)
    print("Your final score: ",p.score)
chm='Y'
while(chm.upper()=="Y"):
    os.system('cls')
    gamePlay()
    chm=input("Play again?(Y/N):" )
