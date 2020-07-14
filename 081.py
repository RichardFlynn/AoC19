from collections import Counter
image=input()
layers=[]
width=25
height=6
layers.append(list(list(list(map(int,[image[x] for x in range(width*y,width*y+width)]))for y in range(height*z,height*z+height))for z in range(int(len(image)/(height*width)))))

smallest=sum(Counter(layers[0][0][x])[0] for x in range(height))+1
ans="ERROR"
for i in layers[0]:
    if sum(Counter(i[x])[0] for x in range(height))<smallest:
        smallest=sum(Counter(i[x])[0] for x in range(height))
        ans=sum(Counter(i[x])[1] for x in range(height))*sum(Counter(i[x])[2] for x in range(height))
print(smallest)
print(ans)
