
import json
from TagMapper import TagMapper
from TagMapperClosing import TagMapperClosing
from IdentifierList import IdentifierList


# Global Variables
openingTags = TagMapper()
closingTags = TagMapperClosing()
idType = IdentifierList()


def defaultTagSetup():
    htmlFile.write(openingTags.htmlVersionSpecifier)
    htmlFile.write(openingTags.head)
    htmlFile.write(openingTags.cssLink)
    htmlFile.write(closingTags.head)
    htmlFile.write(openingTags.body)


def addClosingTags():
    htmlFile.write(closingTags.body)
    htmlFile.write(closingTags.html)
    htmlFile.close()
    cssFile.close()


def createDoc():
    global htmlFile, cssFile
    htmlFile = open("sample.html", "w")
    cssFile = open("sample.css", "w")


def fetchConfigData():
    global designJsonData
    with open('/Users/hasundaram/Desktop/ScreenDesignProject/sreenDesignData.json') as jsonFile:
        designJsonData = json.load(jsonFile)


def parseConfigData():
    index = 0
    for item in designJsonData:
        print(item)
    while index < len(designJsonData):
        item = designJsonData[index]
        keyList = list(item.keys())
        if idType.type in keyList:
            index = analyzeNodeType(item, index)
            cssFile.write("\n" + item[idType.layerStyle])
        index += 1


def analyzeNodeType(item, index):
    elementType = ''
    if 'button' in item[idType.name]:
        createButtonCode(item, index)
        return index + 1
    elif 'text' in item[idType.type]:
        createTextCode(item)
    return index


def createButtonCode(item, index):
    global htmlFile
    nextItem = designJsonData[index + 1]
    className = item[idType.layerStyle].split()[0].strip(".")
    htmlFile.write(openingTags.button + className + '">' + nextItem[idType.name])
    htmlFile.write(closingTags.button)


def createTextCode(item):
    global htmlFile
    className = item[idType.layerStyle].split()[0].strip(".")
    htmlFile.write(openingTags.div + className + '">' + item[idType.name])
    htmlFile.write(closingTags.div)


def mainFunc():
    fetchConfigData()
    createDoc()
    defaultTagSetup()
    parseConfigData()
    addClosingTags()

mainFunc()



