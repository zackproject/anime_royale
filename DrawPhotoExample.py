from unittest import result
from PIL import Image, ImageDraw, ImageFont
from RoyaleKeys import keys

# Size text where is most viewest


def sizeTextCenter(W, H):
    if W > H:
        return W
    else:
        return 10


def centerText(W, H):
    if W > H:
        return (int(H/2), int(-W/2))
    else:
        return (int(0), int(-W/2))


def copiaFoto():
    locationImage = keys["path"]["img_asesino"]
    msg = keys["eliminated_image"]["text"]
    mfontText = keys["eliminated_image"]["font"]
    mColor = keys["eliminated_image"]["color"]
    locationImage = keys["path"]["img_asesino"]
    msg = keys["eliminated_image"]["text"]
    mfontText = keys["eliminated_image"]["font"]
    mColor = keys["eliminated_image"]["color"]
    im = Image.open(locationImage).convert('RGBA')
    W, H = im.size
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg)
    mfont = ImageFont.truetype(mfontText, sizeTextCenter(W, H))
    draw.text(centerText(W, H), msg, fill=mColor, font=mfont)
    im.save(keys["path"]["img_victima"], "PNG")
    print("W:{} H:{}    w:{} h:{}".format(W, H, w, h))


copiaFoto()
