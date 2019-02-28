import json


filename= 'gameState.json'


def saveJsom(string):
    newJson = json.dumps(string)
    with open(filename, "w") as file:
        file.write(newJson)


def getGameStateJson():
    content = ''
    with open(filename) as file:
        for line in file:
            content += line
    return content


