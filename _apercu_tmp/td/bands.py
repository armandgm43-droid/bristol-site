import numpy as np, sys
from PIL import Image, ImageFilter
def load(f, photo=False):
    im=Image.open(f).convert('L')
    if photo:
        bg=im.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(25))
        a=np.asarray(im,float)/np.maximum(np.asarray(bg,float),1)
        a=np.clip((a-0.45)/(0.80-0.45),0,1)*255
        return a
    return np.asarray(im,float)
f=sys.argv[1]; photo=len(sys.argv)>2
a=load(f,photo)
if photo: Image.fromarray(a.astype(np.uint8)).save(f.replace('.png','-norm.png'))
d=a<140; d[:,:12]=False
if photo: d[:,:245]=False; d[:,1420:]=False; d[1850:,:]=False
rows=d.sum(1)>=2
y=0;H=len(rows)
while y<H:
    if rows[y]:
        y0=y
        while y<H and rows[y]: y+=1
        cols=np.where(d[y0:y].sum(0)>0)[0]
        print(f"{y0}-{y}  x {cols[0]}-{cols[-1]}")
    y+=1
