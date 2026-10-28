import sys, glob, os
from PIL import Image, ImageDraw
pat=sys.argv[1]; out=sys.argv[2]
fs=sorted(glob.glob(pat))
ims=[Image.open(f).convert('RGB') for f in fs]
W=max(i.width for i in ims); H=sum(i.height+30 for i in ims)
m=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(m); y=0
for f,i in zip(fs,ims):
    d.rectangle((0,y,W,y+28),fill=(255,220,220)); d.text((4,y+8),os.path.basename(f),fill=(200,0,0)); y+=30
    m.paste(i,(0,y)); d.rectangle((0,y,i.width-1,y+i.height-1),outline=(0,0,255)); y+=i.height
m=m.resize((int(W*0.7),int(H*0.7)))
m.save(out); print(m.size)
