def FFT(inp):
    out=""
    for i in range(len(inp)):
        pat=[]
        while len(pat)-1<len(inp):
            pat.extend(list(0 for x in range(i+1)))
            if len(pat)-1>len(inp):
                break
            pat.extend(list(1 for x in range(i+1)))
            if len(pat)-1>len(inp):
                break
            pat.extend(list(0 for x in range(i+1)))
            if len(pat)-1>len(inp):
                break
            pat.extend(list(-1 for x in range(i+1)))
        #print(len(pat),len(inp))
        on=0
        for j in range(len(inp)):
            #print(on)
            on+=int(inp[j])*pat[j+1]
        out+=str(abs(on)%10)
        #print(out)
    return out
pattern=[0,1,0,-1]

num=input()
num=num*10000
for _ in range(100):
    num=FFT(num)
    
print(num[303673:303681])