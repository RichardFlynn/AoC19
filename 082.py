from collections import Counter
image=input()
layers=[]
width=25
height=6
layers.append(list(list(list(map(int,[image[x] for x in range(width*y,width*y+width)]))for y in range(height*z,height*z+height))for z in range(int(len(image)/(height*width)))))
print(layers[0])
realimage=[]
realimage.append(list([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] for x in range(6)))
print(realimage)
for h in range(width):
    for i in range(height):
        for j in layers[0]:
            if j[i][h]!=2:
                realimage[0][i][h]=j[i][h]
                break
#             print(j[i][h])
#         print("")
for i in realimage[0]:
    print(i)