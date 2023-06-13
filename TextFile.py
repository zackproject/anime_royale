from RoyaleKeys import keys
import os
def saveTweetText(asesino, eliminado, restantes):
    rutaTxt = keys["path"]["txt_info"]
    text = keys["twitter"]["text"]["battle_3_items"].format(
        asesino, eliminado, restantes)
    with open(rutaTxt, 'w') as filetowrite:
        filetowrite.write(text)
    filetowrite.close


def getTextFromFile(pathTxt):
    createFileIsDoesNoExist(pathTxt)
    f = open(pathTxt, "r")
    textReading = f.read()
    f.close
    return textReading


def checkIsGameAvaliable():
    textEmergencia = getTextFromFile(keys["path"]["txt_info"])
    secretCode = keys["secret_code_stop_bot"]
    if textEmergencia != secretCode:
        return True
    else:
        return False


def saveCodeOnFile():
    rutaTxt = keys["path"]["txt_info"]
    secretCode = keys["secret_code_stop_bot"]
    with open(rutaTxt, 'w') as filetowrite:
        filetowrite.write(secretCode)
    filetowrite.close


def createFileIsDoesNoExist(filename):
    if not os.path.exists(filename):
        open(filename, 'w').close()
