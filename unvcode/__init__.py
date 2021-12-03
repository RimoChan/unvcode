import os
import functools
import unicodedata
from typing import Tuple

import numpy as np
from PIL import Image, ImageDraw, ImageFont


此處 = os.path.abspath(os.path.dirname(__file__))
font = f'{此處}/NotoSerifSC-SemiBold.otf'

d = {}
for i in range(65536):
    字 = chr(i)
    新字 = unicodedata.normalize('NFKC', 字)
    if 字 != 新字:
        d.setdefault(新字, []).append(字)

@functools.lru_cache()
def 画皮(字):
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    fnt = ImageFont.truetype(font, 64)
    d = ImageDraw.Draw(img)
    d.text((0, 0), 字, font=fnt, fill=(0, 0, 0))
    return np.asarray(img)/255


def 比较(字1, 字2):
    return (画皮(字1)-画皮(字2)).var()


def 假面(字, skip_ascii, mse):
    if ord(字) < 128 and skip_ascii:
        return None, 字
    候选组 = d.get(字, [])
    差异组 = [比较(字, i) for i in 候选组]
    if not 候选组:
        return None, 字
    差异, 新字 = min(zip(差异组, 候选组))
    if 差异 > mse:
        return None, 字
    return 差异, 新字


def unvcode(s: str, skip_ascii=True, mse=0.1) -> Tuple[str, Tuple[float, ...]]:
    差异, 串 = zip(*[假面(i, skip_ascii, mse) for i in s])
    return ''.join(串), 差异
