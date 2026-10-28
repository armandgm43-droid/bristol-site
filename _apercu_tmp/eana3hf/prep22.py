import numpy as np
from PIL import Image, ImageFilter
def prep(path, angle):
    im = Image.open(path).convert('L').rotate(-90, expand=True)
    im = im.rotate(angle, resample=Image.BICUBIC, fillcolor=255)
    # aplatissement du fond : fond estimé par filtre max sur image réduite
    small = im.resize((im.width // 16, im.height // 16), Image.BILINEAR)
    bg = small.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(4)).resize(im.size, Image.BILINEAR)
    a = np.asarray(im, float) / np.maximum(np.asarray(bg, float), 1)
    a = np.clip((a - 0.35) / (0.85 - 0.35), 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8))
for i, ang in ((1, 0.8), (2, 0.7)):
    p = prep('sources/eana3/annales/2022-2023-partiel-circuits-hf-oscillateurs-p%d.jpg' % i, ang)
    p.save('_apercu_tmp/eana3hf/grid/d22-p%d.png' % i)
    p.resize((p.width//2, p.height//2)).save('_apercu_tmp/eana3hf/grid/d22h-p%d.png' % i)
