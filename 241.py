def update(p):
    
    temp=list(list(2 for x in range(7))for y in range(7))
    for y in range(7):
        for x in range(7):
            temp[y][x]=p[y][x]
    #temp.extend(list(x for x in p))
    #temp[0][0]=3
    #print(p)
    for y in range(1,6):
        for x in range(1,6):
            
            if temp[y][x]==1:
                if temp[y-1][x]+temp[y+1][x]+temp[y][x-1]+temp[y][x+1]!=1:
                    p[y][x]=0
            elif temp[y][x]==0:
                if temp[y-1][x]+temp[y+1][x]+temp[y][x-1]+temp[y][x+1] in(1,2):
                    p[y][x]=1
    
states=[]#[[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0]]]
eris=[[0,0,0,0,0,0,0],[0,0,1,0,1,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0]]
# for i in range(7):
#     print(eris[i])
count=0
while True:
    #print("h")
    update(eris)
    #print(eris)
    if eris in states:#== [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0]]:
        #print(eris)
        #print(states)
        break
    #print(eris)
    states.append(list(list(eris[y][x]for x in range(7))for y in range(7)))
    
    count+=1
# for i in range(7):
#     print(eris[i])
print(states)
print(count)
value=1
bio=0
for y in range(1,6):
    for x in range(1,6):
        if eris[y][x]:
            bio+=value
        value*=2
print(bio)