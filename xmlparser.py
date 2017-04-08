from xml.dom import minidom
from os import listdir, rename
from os.path import isfile, join
import pickle
PATH = "rawXMLs"
class Wrapper:
    def __init__(self, value):
        self.value=value
DRPNames = [""]
numDrps = 9
('hasCustComp', 'hasRegAction', 'hasBankrupt', 'hasCriminal', 'hasCivilJudc', 'hasBond', 'hasInvstgn', 'hasJudgment', 'hasTermination')
if __name__ == "__main__":
    listOfFiles = sorted([f for f in listdir(PATH) if isfile(join(PATH, f))])#["testData/354962.json"]
    print listOfFiles
    allIndividuals = []
    for fileName in listOfFiles[:10]:
        #if "s8" in fileName:break
        individuals = minidom.parse(join(PATH, fileName)).getElementsByTagName("Indvl")
        for individual in individuals:
            try:
                infoField = individual.getElementsByTagName("Info")[0]
                nameData = (infoField.attributes['lastNm'].value, infoField.attributes['firstNm'].value, int(infoField.attributes['indvlPK'].value))
                employmentHistory = []
                for workPlace in individual.getElementsByTagName("EmpHs"):
                    place = (workPlace.attributes["orgNm"].value, workPlace.attributes.get("city",Wrapper("N/A")).value, workPlace.attributes.get("state",Wrapper("N/A")).value)
                    timeSpan = (workPlace.attributes["fromDt"].value, workPlace.attributes.get("toDt",Wrapper("04/2017")).value)
                    employmentHistory.append((place, timeSpan))
                drps = individual.getElementsByTagName("DRP")
                drpVals = [False for i in range(numDrps)]
                if drps:
                    drpVals = [a[1]=="Y" for a in sorted(drps[0].attributes.items(), key = lambda a: a[0])]
                allIndividuals.append((nameData,employmentHistory, drpVals ))
            except Exception as e:
                print e
        print fileName
    pickle.dump(allIndividuals, open("consolodatedOutput.pic", "w"))
