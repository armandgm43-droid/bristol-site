import sys,glob
from PIL import Image, ImageDraw
fs=sys.argv[2:]; ims=[Image.open(f).convert('L') for f in fs]
w=max(i.width for i in ims); h=sum(i.height+30 for i in ims)
out=Image.new('L',(w,h),200); y=0; d=ImageDraw.Draw(out)
for f,i in zip(fs,ims):
    d.text((5,y+5),f.split('/')[-1],fill=0); y+=30; out.paste(i,(0,y)); y+=i.height
out.save(sys.argv[1])
