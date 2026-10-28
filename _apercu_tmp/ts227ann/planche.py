import sys, glob, re
from PIL import Image, ImageDraw
# planche.py out_prefix files... ; splits into sheets of max height 2400
files=sys.argv[2:]
def key(f):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)',f)]
files=sorted(files,key=key)
sheets=[];cur=[];h=0
for f in files:
    im=Image.open(f).convert('RGB')
    if h+im.height+30>2400 and cur: sheets.append(cur);cur=[];h=0
    cur.append((f,im));h+=im.height+30
sheets.append(cur)
for i,s in enumerate(sheets):
    W=max(im.width for _,im in s)+10
    out=Image.new('RGB',(W,sum(im.height+30 for _,im in s)),(255,255,255))
    d=ImageDraw.Draw(out);y=0
    for f,im in s:
        d.rectangle([0,y,W,y+28],fill=(255,220,220)); d.text((5,y+8),f.split('/')[-1],fill=(200,0,0))
        out.paste(im,(5,y+29)); y+=im.height+30
    out.save(f'{sys.argv[1]}-{i}.png'); print(f'{sys.argv[1]}-{i}.png', out.size)
