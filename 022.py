def checksec():
    
    points1.add((x1,y1))
    points2.add((x2,y2))
strucs1=input().split(",")
strucs2=input().split(",")

points1=set()
points2=set()

x1=0
y1=0
x2=0
y2=0

for i in strucs1:
    x2=0
    y2=0
    if i[0]=="U":
        for x in range(int(i[1:])):
            y1+=1
            #print(x1,y1)
            checksec()
    elif i[0]=="R":
        for x in range(int(i[1:])):
            x1+=1;
            #print(x1,y1)
            checksec()
    elif i[0]=="D":
        for x in range(int(i[1:])):
            y1-=1
            #print(x1,y1)
            checksec()
    elif i[0]=="L":
        for x in range(int(i[1:])):
            x1-=1
            #print(x1,y1)
            checksec()
for j in strucs2:
    if j[0]=="U":
        for x in range(int(j[1:])):
            y2+=1;
            #print(x2,y2)
            checksec()
    elif j[0]=="R":
        for x in range(int(j[1:])):
            x2+=1;
            #print(x2,y2)
            checksec()
    elif j[0]=="D":
        for x in range(int(j[1:])):
            y2-=1;
            #print(x2,y2)
            checksec()
    elif j[0]=="L":
        for x in range(int(j[1:])):
            x2-=1;
            #print(x2,y2)
            checksec()
secs=[]
for x in points1:
    if x in points2:
        #print(x)
        secs.append(abs(x[0])+abs(x[1]))
print(min(secs))