
import json


filename = 'gameState.json'


def toJson(string):
    newJson = json.dumps(string)
    return newJson


def fromJson(jsonfile):
    save = json.loads(jsonfile)
    return save


def saveGameState(state, file):
    with open(file, "w") as file:
        file.write(state)


def getGameState(file):
    content = ''
    with open(file) as f:
        for line in f:
            content += line.rstrip('\r\n')
    return content

