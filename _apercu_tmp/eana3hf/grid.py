import sys, subprocess, os, numpy as np
from PIL import Image, ImageDraw
# usage: grid.py pdf page out y0 y1 [x0 x1] [step]
pdf, pg, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
y0, y1 = int(sys.argv[4]), int(sys.argv[5])
x0 = int(sys.argv[6]) if len(sys.argv)>6 else 0
x1 = int(sys.argv[7]) if len(sys.argv)>7 else 99999
step = int(sys.argv[8]) if len(sys.argv)>8 else 20
if pdf.endswith('.png') or pdf.endswith('.jpg'):
    im = Image.open(pdf).convert('L')
else:
    cache = out + '.full.png'
    base = os.path.expanduser('~/gridtmp')
    subprocess.run(['pdftoppm','-r','200','-f',str(pg),'-l',str(pg),'-singlefile','-gray','-png',pdf,base],check=True)
    im = Image.open(base+'.png').convert('L')
x1 = min(x1, im.width)
c = im.crop((x0,y0,x1,y1)).convert('RGB')
d = ImageDraw.Draw(c)
for y in range(0, y1-y0, step):
    col = (255,0,0) if (y0+y)%100==0 else (255,180,180)
    d.line([(0,y),(25 if (y0+y)%100 else 60,y)], fill=col)
    if (y0+y)%100==0: d.text((62,y-5), str(y0+y), fill=(255,0,0))
for x in range(0, x1-x0, 100):
    d.line([(x,0),(x,12)], fill=(0,0,255)); d.text((x+2,12), str(x0+x), fill=(0,0,255))
c.save(out)
print(c.size)
