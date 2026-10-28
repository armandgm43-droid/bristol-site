import sys
from PIL import Image, ImageDraw
# usage: grid.py src out y0 y1 [x0 x1]
src,out,y0,y1=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
im=Image.open(src).convert('RGB')
x0,x1=(int(sys.argv[5]),int(sys.argv[6])) if len(sys.argv)>6 else (0,im.width)
c=im.crop((x0,y0,x1,y1)).copy()
d=ImageDraw.Draw(c)
for y in range((y0//25+1)*25,y1,25):
    col=(255,0,0) if y%100==0 else ((0,160,0) if y%50==0 else (180,180,255))
    d.line([(0,y-y0),(60,y-y0)],fill=col,width=2)
    d.line([(c.width-60,y-y0),(c.width,y-y0)],fill=col,width=2)
    if y%50==0: d.text((62,y-y0-6),str(y),fill=col)
for x in range((x0//100+1)*100,x1,100):
    d.line([(x-x0,0),(x-x0,15)],fill=(255,0,0),width=2); d.text((x-x0+2,16),str(x),fill=(255,0,0))
c.save(out)
