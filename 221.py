from sys import stdin

decklen=10007
deck=list(x for x in range(decklen))
#print(deck)
strucs=[]
for i in stdin:
    if i=="\n":
        break
    j=i.strip()
    if j[0]=='c':
        strucs.append('c'+j[4:])
    elif j[5]=='i':
        strucs.append('n')
    elif j[5]=='w':
        strucs.append("d"+j[20:])
    else:
        print("INPUT ERROR")

#print(strucs)
for i in strucs:
    if i=='n':
        deck=[deck[decklen-1-x]for x in range(decklen)]
    elif i[0]=='c':
        deck=[deck[(x+int(i[1:]))%decklen] for x in range(decklen)]
    elif i[0]=='d':
        tempdeck=list(-1 for x in range(decklen))
        for j in range(decklen):
            tempdeck[(int(i[1:])*j)%decklen]=deck[j]
        deck=tempdeck[0:]
        
#print(deck)
for i in range(decklen):
    if deck[i]==2019:
        print(i)
        break
    