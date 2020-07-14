from anytree import *
from sys import stdin

class Base():
    foo=4
class RecipeNodes(Base,NodeMixin):
    def __init__(self,name,out_quant,in_quant,parent=None,children=None):
        super(RecipeNodes, self).__init__()
        self.name = name
        self.out_quant = out_quant
        self.in_quant = in_quant
        self.parent = parent
        if children:
            self.children = children

recipes=[]
for i in stdin:
    if i=="\n":
        break
    recipes.append(i.strip().split("=>"))
    
dict={}

print(recipes)
while len(dict)<len(recipes):
    for i in recipes:
        endchem=i[1].strip().split(" ")
        #print(endchem)
        dict[endchem[1]]=Node(endchem[1])
    for i in range(len(recipes)):
        endchem=recipes[len(recipes)-1-i][1].strip().split(" ")
        print(endchem)
        print(recipes[len(recipes)-1-i])
        #print(dict)
        if recipes[len(recipes)-1-i][0].split(" ")[1]!='ORE':
            startchems=list(map(lambda x:x.strip().split(" "),recipes[len(recipes)-1-i][0].split(",")))
            for j in range(len(startchems)):
                dict[startchems[len(startchems)-1-j][1]].parent=dict[endchem[1]]
        else:
            dict["ORE"]=Node("ORE",parent=dict[endchem[1]])
    break
print(dict)
print(RenderTree(dict['FUEL']))
    
#print(recipes)