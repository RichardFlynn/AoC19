codess=input().split(",")



def amplify(inputs,codesss,phases):
    for x in range(5):
        i=0
        inputs.append(phases[x])
        codes=codesss[:]
#         print(codes)
        while True:
#             print(i)
#             print(codes[i:i+5])
#             print(inputs)
            if codes[i][len(codes[i])-1]=="1":
                while len(codes[i])<5:
                    codes[i]="0"+codes[i]
                if codes[i][len(codes[i])-3]=="1":
                    a=i+1
                elif codes[i][len(codes[i])-3]=="0":
                    a=int(codes[i+1])
                else:
                    print("ERROR1")
                    break
                if codes[i][len(codes[i])-4]=="1":
                    b=i+2
                elif codes[i][len(codes[i])-4]=="0":
                    b=int(codes[int(i+2)])
                else:
                    print("ERROR2")
                    break
                if codes[i][len(codes[i])-5]=="1":
                    c=i+3
                elif codes[i][len(codes[i])-5]=="0":
                    c=int(codes[int(i+3)])
                else:
                    print("ERROR3")
                    break
                #print(a,b,c)
                codes[c]=str(int(codes[b])+int(codes[a]))
                i+=4
            elif codes[i][len(codes[i])-1]=="2":
                while len(codes[i])<5:
                    codes[i]="0"+codes[i]
                if codes[i][len(codes[i])-3]=="1":
                    a=i+1
                elif codes[i][len(codes[i])-3]=="0":
                    a=int(codes[i+1])
                else:
                    print("ERROR4")
                    break
                if codes[i][len(codes[i])-4]=="1":
                    b=i+2
                elif codes[i][len(codes[i])-4]=="0":
                    b=int(codes[i+2])
                else:
                    print("ERROR5")
                    break
                if codes[i][len(codes[i])-5]=="1":
                    c=i+3
                elif codes[i][len(codes[i])-5]=="0":
                    c=int(codes[i+3])
                else:
                    print("ERROR6")
                    break
                codes[c]=str(int(codes[b])*int(codes[a]))
                i+=4
            elif codes[i][len(codes[i])-1]=="3":
                codes[int(codes[i+1])]=inputs.pop(len(inputs)-1)
                i+=2
            elif codes[i][len(codes[i])-1]=="4":
                inputs.append(int(codes[int(codes[i+1])]))
                #print(codes[int(codes[i+1])])
                i+=2
            elif codes[i][len(codes[i])-1]=="5":
                while len(codes[i])<4:
                    codes[i]= "0"+codes[i]
                if codes[i][len(codes[i])-3]=="1":
                    a=i+1
                elif codes[i][len(codes[i])-3]=="0":
                    a=int(codes[i+1])
                else:
                    print("ERROR4")
                    break
                if codes[i][len(codes[i])-4]=="1":
                    b=i+2
                elif codes[i][len(codes[i])-4]=="0":
                    b=int(codes[i+2])
                else:
                    print("ERROR5")
                    break
                if int(codes[a])!=0:
                    i=int(codes[b])
                else:
                    i+=3
            elif codes[i][len(codes[i])-1]=="6":
                while len(codes[i])<4:
                    codes[i]= "0"+codes[i]
                if codes[i][len(codes[i])-3]=="1":
                    a=i+1
                elif codes[i][len(codes[i])-3]=="0":
                    a=int(codes[i+1])
                else:
                    print("ERROR4")
                    break
                if codes[i][len(codes[i])-4]=="1":
                    b=i+2
                elif codes[i][len(codes[i])-4]=="0":
                    b=int(codes[i+2])
                else:
                    print("ERROR5")
                    break
                if int(codes[a])==0:
                    i=int(codes[b])
                else:
                    i+=3
            elif codes[i][len(codes[i])-1]=="7":
                while len(codes[i])<5:
                    codes[i]= "0"+codes[i]
                if codes[i][len(codes[i])-3]=="1":
                    a=i+1
                elif codes[i][len(codes[i])-3]=="0":
                    a=int(codes[i+1])
                else:
                    print("ERROR4")
                    break
                if codes[i][len(codes[i])-4]=="1":
                    b=i+2
                elif codes[i][len(codes[i])-4]=="0":
                    b=int(codes[i+2])
                else:
                    print("ERROR5")
                    break
                if codes[i][len(codes[i])-5]=="1":
                    c=i+3
                elif codes[i][len(codes[i])-5]=="0":
                    c=int(codes[i+3])
                else:
                    print("ERROR6")
                    break
                if int(codes[a])<int(codes[b]):
                    codes[c]="1"
                else:
                    codes[c]="0"
                i+=4
            elif codes[i][len(codes[i])-1]=="8":
                while len(codes[i])<5:
                    codes[i]= "0"+codes[i]
                if codes[i][len(codes[i])-3]=="1":
                    a=i+1
                elif codes[i][len(codes[i])-3]=="0":
                    a=int(codes[i+1])
                else:
                    print("ERROR4")
                    break
                if codes[i][len(codes[i])-4]=="1":
                    b=i+2
                elif codes[i][len(codes[i])-4]=="0":
                    b=int(codes[i+2])
                else:
                    print("ERROR5")
                    break
                if codes[i][len(codes[i])-5]=="1":
                    c=i+3
                elif codes[i][len(codes[i])-5]=="0":
                    c=int(codes[i+3])
                else:
                    print("ERROR6")
                    break
                if int(codes[a])==int(codes[b]):
                    codes[c]="1"
                else:
                    codes[c]="0"
                i+=4
            elif codes[i]=="99":
                break
            else:
                print("ERROR7")
                print(codes[:i])
                break
    return inputs

outputs=[]
for h in range(5):
    for j in range(5):
        if h!=j:
            for k in range(5):
                if j!=k and h!=k:
                    for l in range(5):
                        if l not in (h,j,k):
                            for m in range(5):
                                if m not in (h,j,k,l):
                                    outputs.append(amplify([0],codess,(h,j,k,l,m)))
print(max(outputs))