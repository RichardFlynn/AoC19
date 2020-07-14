def checksec():
    dic1[(x1,y1)]=steps1
    points1.add((x1,y1))
def checksec2():
    dic2[(x2,y2)]=steps2
    points2.add((x2,y2))
strucs1=input().split(",")
strucs2=input().split(",")

dic1={}
dic2={}

steps1=0
steps2=0

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
            steps1+=1
            checksec()
    elif i[0]=="R":
        for x in range(int(i[1:])):
            x1+=1;
            steps1+=1
            checksec()
    elif i[0]=="D":
        for x in range(int(i[1:])):
            y1-=1
            steps1+=1
            checksec()
    elif i[0]=="L":
        for x in range(int(i[1:])):
            x1-=1
            steps1+=1
            checksec()
for j in strucs2:
    if j[0]=="U":
        for x in range(int(j[1:])):
            y2+=1;
            steps2+=1
            checksec2()
    elif j[0]=="R":
        for x in range(int(j[1:])):
            x2+=1;
            steps2+=1
            checksec2()
    elif j[0]=="D":
        for x in range(int(j[1:])):
            y2-=1;
            steps2+=1
            checksec2()
    elif j[0]=="L":
        for x in range(int(j[1:])):
            x2-=1;
            steps2+=1
            checksec2()
secs=[]
for x in points1:
    if x in points2:
        secs.append(dic1[x]+dic2[x])
        #print(x)
        #secs.append(abs(x[0])+abs(x[1]))
print(min(secs))