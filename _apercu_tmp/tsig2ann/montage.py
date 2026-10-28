import sys, glob
from PIL import Image, ImageDraw
files=sys.argv[2:]; out=sys.argv[1]
ims=[Image.open(f).convert('RGB') for f in files]
w=max(i.width for i in ims); h=sum(i.height+30 for i in ims)
o=Image.new('RGB',(w,h),(255,255,255)); d=ImageDraw.Draw(o); y=0
for f,i in zip(files,ims):
    d.rectangle([0,y,w,y+28],fill=(255,220,220)); d.text((5,y+8),f.split('/')[-1]+' '+str(i.size),fill=(200,0,0)); y+=30
    o.paste(i,(0,y)); d.rectangle([0,y,i.width-1,y+i.height-1],outline=(0,160,0)); y+=i.height
o.save(out)
