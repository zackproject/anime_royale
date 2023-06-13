from PIL import Image, ImageDraw, ImageFont
from RoyaleKeys import keys
import requests
from Character import Character


def generatePanelImage(characterList):
    separator = keys["panel_royale"]["text"]["separator"]
    # El titulo tiene el separadoe delante y detras
    titulo = "{1}\n {0}\n{1}\n".format(
        keys["panel_royale"]["text"]["title"], separator)
    # Fill the ranklist with all, alive , eliminated,
    rankList = makeRanking(characterList)
    # El piePagina tiene el separador delante y detras
    elementsFooter = (keys["panel_royale"]["text"]["footer_3_items"]).format(
        rankList[0], rankList[1], rankList[2])
    piePagina = "{1}\n {0}\n{1}\n".format(elementsFooter, separator)
    #I cant order by name by query table, so i order here
    characterList.sort(key=lambda x: x.name)
# Convert to text all names alives and elimated 'replaced'
    textAlive = namesAliveToText(characterList)
    textEliminated = namesEliminatedToText(characterList)
    # Para el panel generamos el texto dos veces uno en un color para vivos y otro sobrepuesto de otro color para eliminados
    img = Image.new('RGB', (
        keys["panel_royale"]["width"],
        keys["panel_royale"]["height"]),
        color=keys["panel_royale"]["color"]["background"])
    # El tipo de letra debe ser mono(espaciado) para que los espacion coincidan
    fnt = ImageFont.truetype(
        keys["panel_royale"]["text"]["font"],
        keys["panel_royale"]["text"]["size_text"], encoding="unic")
    d = ImageDraw.Draw(img)
    #Margin out panel royale and text
    margin = keys["panel_royale"]["margin"]
    # Generamos el texto de vivos con el titulo y el pie de pagina de un color
    d.text((margin, margin), titulo + textAlive+"\n"+piePagina, font=fnt,
           fill=(keys["panel_royale"]["color"]["alive"]))
    # Generamos el texto de eliminados (respetando \n del titulo y pie) de otro color
    d.text((margin, margin), "\n\n\n" + textEliminated, font=fnt,
           fill=(keys["panel_royale"]["color"]["eliminated"]))
    # Guarda la imagen
    imageName = keys["path"]["img_panel"]
    img.save(imageName)
    print('Image generated = '+imageName)


# Draw a cross in a image
def generateImgEliminated():
    locationImage = keys["path"]["img_victima"]
    mtext = keys["eliminated_image"]["text"]
    mfontText = keys["eliminated_image"]["font"]
    mcolor = keys["eliminated_image"]["color"]
    #mcolor = (255, 255, 255, 0)
    base = Image.open(locationImage).convert('RGBA')
    width, height = base.size
    txt = Image.new('RGBA', base.size, mcolor)
    fnt = ImageFont.truetype(mfontText, height, encoding="unic")
    d = ImageDraw.Draw(txt)
    w, h = d.textsize(mtext, font=fnt)
    # Center the letter "x" or other letter, elimination
    d.text(((width - w) / 2, (height - h)/2),
           mtext, font=fnt, fill=mcolor)
    out = Image.alpha_composite(base, txt)
    rgb_im = out.convert('RGB')
    rgb_im.save(locationImage)


def namesAliveToText(textList):
    # Escribe los nombres seguidos con un salto de linea (/n) cada vez que lo diga
    saltoDeLinea = keys["panel_royale"]["text"]["line_break"]
    num = 0
    text = ""
    for x in textList:
        if num == saltoDeLinea:
            text = text + "\n"
            num = 0
        # The " · " is the symbol to separated the names
        text = text + " · "+(x.name).capitalize()
        num = num + 1
    return text


def namesEliminatedToText(textList):
    # Escribe los nombres seguidos con un salto de linea (/n) cada vez que lo diga
    # Pero si el nombre esta VIVO escribe espacios en blanco en su lugar (otro color)
    text = ""
    num = 0
    saltoDeLinea = keys["panel_royale"]["text"]["line_break"]
    for x in textList:
        if num == saltoDeLinea:
            text = text + "\n"
            num = 0
        # The "  " represent the " · " from namesAliveToText() without the dot
        text = text + "   "+namewithSpaceIsAlive(x)
        num = num + 1
    return text


def namewithSpaceIsAlive(lPerson):
    # Genera espacios en blaco si esta vivo o devuelve (de otro color) el nombre.
    text = ""
    if  lPerson.killer_id== 0:
        no = ""
        for x in range(len(lPerson.name)):
            no = no+" "
        text = text + no
    else:
        text = text + (lPerson.name).capitalize()
    return text


def downImgKiller(urlImage):
    response = requests.get(urlImage)
    path = keys["path"]["img_victima"]
    file = open(path, "wb")
    file.write(response.content)
    file.close()


def downImgVictim(urlImage):
    response = requests.get(urlImage)
    path = keys["path"]["img_asesino"]
    file = open(path, "wb")
    file.write(response.content)
    file.close()


def makeRanking(statusList):
    alived = 0
    total = len(statusList)
    for character in statusList:
        if character.killer_id == 0:
            alived = alived+1
    eliminated = total-alived
    mylist = [total, alived, eliminated]
    return mylist