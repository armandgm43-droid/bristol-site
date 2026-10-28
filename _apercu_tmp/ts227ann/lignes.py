import sys, numpy as np
from PIL import Image
f=sys.argv[1]; x0,x1=int(sys.argv[2]),int(sys.argv[3]); seuil=int(sys.argv[4]) if len(sys.argv)>4 else 120
g=np.asarray(Image.open(f).convert('L'),float)[:,x0:x1]
ink=g<seuil
r=ink.sum(1)>2
ys=np.where(np.diff(np.r_[0,r.astype(int),0])!=0)[0].reshape(-1,2)
out=[]
for a,b in ys:
    c=np.where(ink[a:b].sum(0)>0)[0]
    out.append(f'{a}-{b}[{x0+c[0]}:{x0+c[-1]}]')
print(' '.join(out))
