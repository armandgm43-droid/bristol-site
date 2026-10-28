import sys, numpy as np
from PIL import Image, ImageFilter
f=sys.argv[1]; x0,x1=int(sys.argv[2]),int(sys.argv[3])
im=Image.open(f).convert('L')
g=np.asarray(im,float)
fond=np.asarray(im.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)),float)
a=g/np.maximum(fond,1); ink=(a<0.6).astype(float)
H,W=ink.shape
xs=np.arange(x0,x1); xc=(x0+x1)/2
for yc in range(150,H-150,100):
    best=None
    for s in np.arange(-0.04,0.0401,0.001):
        prof=np.zeros(H+200)
        sub=ink[:,x0:x1]
        # shear: row index y' = y - s*(x-xc)
        for j in range(0,x1-x0,4):
            dy=int(round(s*(xs[j]-xc)))
            col=sub[max(0,yc-120):min(H,yc+120),j]
            prof[100+max(0,yc-120)-dy:100+max(0,yc-120)-dy+len(col)]+=col
        v=(np.diff(prof)**2).sum()
        if best is None or v>best[0]: best=(v,s)
    dens=ink[yc-50:yc+50,x0:x1].mean()
    print(yc, round(best[1],3), round(dens,3))
