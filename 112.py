hull={(0,0):"1"}
robx=0
roby=0
outswitch=True
dire=1

codesinput=input().split(",")
codes={x:codesinput[x] for x in range(len(codesinput))}
relb=0
i=0
#print(codes)
def mem(space):
    for s in space:
        if s not in codes:
            codes[s]="0"
    
while True:
    #mem([i])+relb
    #print(i)
    if codes[i]=="99":
        break
    elif codes[i][len(codes[i])-1]=="1":
        while len(codes[i])<5:
            codes[i]="0"+codes[i]
        if codes[i][len(codes[i])-3]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][len(codes[i])-3]=="1":
            a=i+1
        elif codes[i][len(codes[i])-3]=="0":
            a=int(codes[i+1])
        else:
            print("ERROR1")
            break
        if codes[i][len(codes[i])-4]=="2":
            b=int(codes[int(i+2)])+relb
        elif codes[i][len(codes[i])-4]=="1":
            b=i+2
        elif codes[i][len(codes[i])-4]=="0":
            b=int(codes[int(i+2)])
        else:
            print("ERROR2")
            break
        if codes[i][len(codes[i])-5]=="2":
            c=int(codes[int(i+3)])+relb
        elif codes[i][len(codes[i])-5]=="1":
            c=i+3
        elif codes[i][len(codes[i])-5]=="0":
            c=int(codes[int(i+3)])
        else:
            print("ERROR3")
            break
        #print([a,b,c])
        mem([a,b,c])        
        codes[c]=str(int(codes[b])+int(codes[a]))
        i+=4
    elif codes[i][len(codes[i])-1]=="2":
        while len(codes[i])<5:
            codes[i]="0"+codes[i]
        if codes[i][len(codes[i])-3]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][len(codes[i])-3]=="1":
            a=i+1
        elif codes[i][len(codes[i])-3]=="0":
            a=int(codes[i+1])
        else:
            print("ERROR4")
            break
        if codes[i][len(codes[i])-4]=="2":
            b=int(codes[i+2])+relb
        elif codes[i][len(codes[i])-4]=="1":
            b=i+2
        elif codes[i][len(codes[i])-4]=="0":
            b=int(codes[i+2])
        else:
            print("ERROR5")
            break
        if codes[i][len(codes[i])-5]=="2":
            c=int(codes[i+3])+relb
        elif codes[i][len(codes[i])-5]=="1":
            c=i+3
        elif codes[i][len(codes[i])-5]=="0":
            c=int(codes[i+3])
        else:
            print("ERROR6")
            break
        mem([a,b,c])
        codes[c]=str(int(codes[b])*int(codes[a]))
        i+=4
    elif codes[i][len(codes[i])-1]=="3":
        while len(codes[i])<3:
            codes[i]="0"+codes[i]
        if codes[i][0]=="2":
            a=int(codes[i+1])+relb
            #print(relb)
        elif codes[i][0]=="1":
            a=i+1
        elif codes[i][0]=="0":    
            a=int(codes[i+1])
        mem([a])
        #print(a)
        #print(codes[a])
        if (robx,roby) not in hull:
            hull[(robx,roby)]=0
        #print("in",hull[(robx,roby)])
        codes[a]=hull[(robx,roby)]
        
        i+=2
    elif codes[i][len(codes[i])-1]=="4":
        while len(codes[i])<3:
            codes[i]="0"+codes[i]
        if codes[i][0]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][0]=="1":
            a=i+1
        elif codes[i][0]=="0":
            a=int(codes[i+1])
        mem([a])
        #print(codes[a])
        if outswitch:
            hull[(robx,roby)]=codes[a]
            #print("paint",codes[a])
        else:
            #print("turn",codes[a])
            if int(codes[a]):
                #print(1)
                dire=(dire+1)%4
            else:
                dire=(dire-1)%4
            if dire%2==0:
                robx+=dire-1
            else:
                roby+=dire*-1+2
            #print("dir",dire)
            #print("loc",(robx,roby))
        outswitch=not outswitch
        i+=2
        #print(dire)
    elif codes[i][len(codes[i])-1]=="5":
        while len(codes[i])<4:
            codes[i]= "0"+codes[i]
        if codes[i][len(codes[i])-3]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][len(codes[i])-3]=="1":
            a=i+1
        elif codes[i][len(codes[i])-3]=="0":
            a=int(codes[i+1])
        else:
            print("ERROR4")
            break
        if codes[i][len(codes[i])-4]=="2":
            b=int(codes[i+2])+relb
        elif codes[i][len(codes[i])-4]=="1":
            b=i+2
        elif codes[i][len(codes[i])-4]=="0":
            b=int(codes[i+2])
        else:
            print("ERROR5")
            break
        mem([a,b])
        if int(codes[a])!=0:
            i=int(codes[b])
        else:
            i+=3
    elif codes[i][len(codes[i])-1]=="6":
        while len(codes[i])<4:
            codes[i]= "0"+codes[i]
        if codes[i][len(codes[i])-3]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][len(codes[i])-3]=="1":
            a=i+1
        elif codes[i][len(codes[i])-3]=="0":
            a=int(codes[i+1])
        else:
            print("ERROR4")
            break
        if codes[i][len(codes[i])-4]=="2":
            b=int(codes[i+2])+relb
        elif codes[i][len(codes[i])-4]=="1":
            b=i+2
        elif codes[i][len(codes[i])-4]=="0":
            b=int(codes[i+2])
        else:
            print("ERROR5")
            break
        mem([a,b])
        if int(codes[a])==0:
            i=int(codes[b])
        else:
            i+=3
    elif codes[i][len(codes[i])-1]=="7":
        while len(codes[i])<5:
            codes[i]= "0"+codes[i]
        if codes[i][len(codes[i])-3]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][len(codes[i])-3]=="1":
            a=i+1
        elif codes[i][len(codes[i])-3]=="0":
            a=int(codes[i+1])
        else:
            print("ERROR4")
            break
        if codes[i][len(codes[i])-4]=="2":
            b=int(codes[i+2])+relb
        elif codes[i][len(codes[i])-4]=="1":
            b=i+2
        elif codes[i][len(codes[i])-4]=="0":
            b=int(codes[i+2])
        else:
            print("ERROR5")
            break
        if codes[i][len(codes[i])-5]=="2":
            c=int(codes[i+3])+relb
        elif codes[i][len(codes[i])-5]=="1":
            c=i+3
        elif codes[i][len(codes[i])-5]=="0":
            c=int(codes[i+3])
        else:
            print("ERROR6")
            break
        mem([a,b,c])
        if int(codes[a])<int(codes[b]):
            codes[c]="1"
        else:
            codes[c]="0"
        i+=4
    elif codes[i][len(codes[i])-1]=="8":
        while len(codes[i])<5:
            codes[i]= "0"+codes[i]
        if codes[i][len(codes[i])-3]=="2":
            a=int(codes[i+1])+relb
        elif codes[i][len(codes[i])-3]=="1":
            a=i+1
        elif codes[i][len(codes[i])-3]=="0":
            a=int(codes[i+1])
        else:
            print("ERROR4")
            break
        if codes[i][len(codes[i])-4]=="2":
            b=int(codes[i+2])+relb
        elif codes[i][len(codes[i])-4]=="1":
            b=i+2
        elif codes[i][len(codes[i])-4]=="0":
            b=int(codes[i+2])
        else:
            print("ERROR5")
            break
        if codes[i][len(codes[i])-5]=="2":
            c=int(codes[i+3])+relb
        elif codes[i][len(codes[i])-5]=="1":
            c=i+3
        elif codes[i][len(codes[i])-5]=="0":
            c=int(codes[i+3])
        else:
            print("ERROR6")
            break
        mem([a,b,c])
        if int(codes[a])==int(codes[b]):
            codes[c]="1"
        else:
            codes[c]="0"
        i+=4
    elif codes[i][len(codes[i])-1]=="9":
        while len(codes[i])<3:
            codes[i]="0"+codes[i]
        if codes[i][0]=="2":
            a=int(codes[i+1])+relb
        if codes[i][0]=="1":
            a=i+1
        elif codes[i][0]=="0":
            a=int(codes[i+1])
        mem([a])
        relb+=int(codes[a])
        i+=2
    else:
        print("ERROR7")
        print(codes[:i])
        break
    #print(i,relb)
#print(codes,relb)
#print(hull)
#print(len(hull))
mark=list(list(0 for x in range(43))for y in range(6))

for x,y in hull.items():
    #print(x[1],x[0],y)
    mark[-x[1]][x[0]]=int(y)
for x in range(6):
    print(mark[x])