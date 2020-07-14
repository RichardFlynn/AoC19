codes=input().split(",")
i=0


while True:
    
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
        codes[int(codes[i+1])]=input()
        i+=2
    elif codes[i][len(codes[i])-1]=="4":
        print(codes[int(codes[i+1])])
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