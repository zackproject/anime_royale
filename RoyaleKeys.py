import json
import sys

def getKeysFromPath(pathJson):
    fileDataJson = open(pathJson, "r")
    keys = json.loads(fileDataJson.read())
    fileDataJson.close
    return keys

def getKeysFromArguments():
    return sys.argv[1]


#Get json from path
paths = "PATH KEYS JSON" #royale_example.json
keys = getKeysFromPath(paths)

#Get json from argument Example: Terminal: python royale.py ./dicts/royale.json
#keys = getKeysFromArguments()

