import sys; from PIL import Image; import numpy as np
f=sys.argv[1]; x0,x1=int(sys.argv[2]),int(sys.argv[3])
a=np.asarray(Image.open(f).convert('L'))[:,x0:x1]<140
rows=a.sum(1)>=2
out=[];y=0;n=len(rows)
while y<n:
    if rows[y]:
        s=y
        while y<n and rows[y]: y+=1
        out.append((s,y))
    y+=1
# merge gaps <6
m=[]
for s,e in out:
    if m and s-m[-1][1]<6: m[-1]=(m[-1][0],e)
    else: m.append((s,e))
print(' '.join(f'{s}-{e}' for s,e in m))
