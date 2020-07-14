from sys import stdin

def check_sur(cur,prev):
    sur=[]
    if rows[cur[0]-1][cur[1]]!='#':
        sur.append(True)
    else:
        sur.append(False)
    if rows[cur[0]][cur[1]+1]!='#':
        sur.append(True)
    else:
        sur.append(False)
    if rows[cur[0]+1][cur[1]]!='#':
        sur.append(True)
    else:
        sur.append(False)
    if rows[cur[0]][cur[1]-1]!='#':
        sur.append(True)
    else:
        sur.append(False)
    return sur

rows=[]
for i in stdin:
    if i=="\n":
        break
    rows.append(list(k for k in i.strip()))
    
print(rows)
start_pos="ERROR" 
start_pos=list((i,j) for j in range(len(rows[i]))for i in range(len(rows))if rows[i][j]=='@')[0]
print(start_pos)
print(check_sur(start_pos,None))
