import math
starish=[]
x=input()
for i in range(5):
    for j in range(5):
        if x[i*5+j]=='#':
            starish.append((j,i))
print(len(starish))
seens=[]
for k in starish:
    total=0
    for l in starish:
        for m in starish:
            print(k,l,m)
            if l==m or k[0]-m[0]/math.gcd(m[0],m[1])==0 or k[1]-m[1]/math.gcd(m[0],m[1])==0:
                continue
            elif abs(k[0]-l[0])%abs(k[0]-m[0]/math.gcd(m[0],m[1]))==0 and abs(k[1]-l[1])%abs(k[1]-m[1]/math.gcd(m[0],m[1]))==0:
                print(abs(k[0]-l[0])%abs(k[0]-m[0]/math.gcd(m[0],m[1])))
                total+=1
                break
    seens.append(10-total)
print(seens)