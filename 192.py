def check(inputs):
    codes={x:codesinput[x] for x in range(len(codesinput))}
    relb=0
    i=0
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
            codes[a]=str(inputs.pop())
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
            return codes[a]
                #print(count)
            #print(codes[a])
            i+=2
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
count=0
codesinput=input().split(",")
codes={x:codesinput[x] for x in range(len(codesinput))}
relb=0
i=0
#print(codes)
def mem(space):
    for s in space:
        if s not in codes:
            codes[s]="0"

sq=True
for x in range(100000):
    for y in range(100000):
        if sq:
            print(x,y-1)
        sq=True
        if int(check([x,y]))==0:
            continue
        for x2 in range(100):
            for y2 in range(100):
                sq=sq and int(check([x+x2,y+y2]))
                if not sq:
                    break
            if not sq:
                break
    
print(codes,relb)
print(count)