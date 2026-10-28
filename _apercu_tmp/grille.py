import sys
from PIL import Image, ImageDraw
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); d = ImageDraw.Draw(im)
for y in range(0, im.height, 50):
    d.line([(0, y), (40, y)], fill=(255, 0, 0), width=2); d.text((42, y - 6), str(y), fill=(255, 0, 0))
    d.line([(im.width - 40, y), (im.width, y)], fill=(255, 0, 0), width=2)
for x in range(0, im.width, 100):
    d.line([(x, 0), (x, 25)], fill=(0, 0, 255), width=2); d.text((x + 2, 26), str(x), fill=(0, 0, 255))
im.save(dst)
