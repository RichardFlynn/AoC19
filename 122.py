def timestep(moonsu):
    moonsu=gravity(moonsu)
    moonsu=move(moonsu)
    return moonsu
        
def gravity(moonsv):
    for m1 in moonsv:
        for m2 in moonsv:
            for i in range(3):
                if m1[i]==m2[i]:
                    continue
                elif m1[i]>m2[i]:
                    m1[i+3]-=1
                elif m1[i]<m2[i]:
                    m1[i+3]+=1
    return moonsv
        
def move(moonsp):
    for m in moonsp:
        for i in range(3):
            m[i]+=m[i+3]
    return moonsp
    
m1=[-13,14,-7,0,0,0]
m2=[-18,9,0,0,0,0]
m3=[0,-3,-3,0,0,0]
m4=[-15,3,-13,0,0,0]

moons=[m1,m2,m3,m4]
#print(moons)
for _ in range(4686774924):
    moons=timestep(moons)
print(moons)
print(sum(sum(abs(i) for i in moons[j][:3])*sum(abs(i) for i in moons[j][3:])for j in range(4)))
