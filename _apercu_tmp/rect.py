import numpy as np
from PIL import Image, ImageOps
def coeffs(dst, src):
    # output (dst) point -> input (src) point
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A.append([x,y,1,0,0,0,-u*x,-u*y]); B.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]); B.append(v)
    return np.linalg.solve(np.array(A,float),np.array(B,float)).tolist()
QUADS={1:([(224.8,328.7),(1360,418),(125.4,1868),(1375,1861.6)]),
       2:([(270,82),(1370,140),(170,1645),(1470,1630)])}
DST={1:[(130,330),(1330,330),(130,1870),(1330,1870)],
     2:[(130,90),(1330,90),(130,1640),(1330,1640)]}
for p in (1,2):
    im=ImageOps.exif_transpose(Image.open('../sources/eaep1/annales/2022-2023-partiel-p%d.jpg'%p)).convert('RGB').resize((1500,2000),Image.LANCZOS)
    c=coeffs(DST[p],QUADS[p])
    out=im.transform((1460,2000),Image.PERSPECTIVE,c,Image.BICUBIC,fillcolor=(255,255,255))
    out.save('eaep1ann/2022-r%d.png'%p)
