import sys, subprocess, os, numpy as np
from PIL import Image, ImageFilter
pdf, page, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
base='/tmp/tsig2flat'
subprocess.run(['pdfimages','-png','-f',str(page),'-l',str(page),pdf,base],check=True)
im=Image.open(base+'-000.png').convert('RGB')
rgb=np.asarray(im,float); R,G,B=rgb[...,0],rgb[...,1],rgb[...,2]
gris=0.299*R+0.587*G+0.114*B
g=Image.fromarray(gris.clip(0,255).astype(np.uint8))
fond=np.asarray(g.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)),float)
a=gris/np.maximum(fond,1)
encre=((B-R)>4)&(a<0.93)
encre=np.asarray(Image.fromarray((encre*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)))>0
noir=(a<0.35)&((B-R)<0)
a[encre&~noir]=1.0
a=np.clip((a-0.45)/(0.88-0.45),0,1)**1.3
o=Image.fromarray((a*255).astype(np.uint8)).convert('RGB')
from PIL import ImageDraw
d=ImageDraw.Draw(o)
for y in range(0,o.height,50):
    d.line([(0,y),(25 if y%100 else 50,y)],fill=(255,0,0),width=2); d.text((52,y-5),str(y),fill=(255,0,0))
for x in range(0,o.width,50):
    d.line([(x,0),(x,25 if x%100 else 50)],fill=(255,0,0),width=2); d.text((x-8,52),str(x),fill=(255,0,0))
o.save(out)
