valid=[]
for x in range(172930,683083):
    doubles=[]
    deccheck=True
    for y in range(5):
        doub=0
        if str(x)[y]>str(x)[y+1]:
            deccheck=False
        #print(str(x)[y])
        for z in range(5):
            if str(x)[y]==str(x)[z]:
                doub+=1
        doubles.append(doub)
    if deccheck and 2 in doubles and len(str(x))==6:
        valid.append(x)
    
print(len(valid))