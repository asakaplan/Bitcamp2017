import json
from os import listdir, rename
from os.path import isfile, join
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features
CREDENTIALS = "credentials.txt"
PATH = "testData"
BAD_PATH = "badData"
def main():
    credentials = eval("\n".join(open(CREDENTIALS, "r").readlines()))

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version="2017-02-27",
        username=credentials["username"],
        password=credentials["password"]
    )

    listOfFiles = [f for f in listdir(PATH) if isfile(join(PATH, f))]#["testData/354962.json"]
    for fileName in listOfFiles:
        fileIn = open(join(PATH, fileName), "r")
        data = json.load(fileIn)
        val = data["html_lawbox"]
        if any(word in val for word in ["convict","acquit","guilty","innocen", "sentenc"]):
            print("Good file: ", fileName)
            for word in ["convict","acquit","guilty","innocen", "sentenc"]:
                if word in val:
                    print "it has ", word
            response = natural_language_understanding.analyze(
                text=data["html_lawbox"],
                features = [features.Entities(), features.Relations()]
            )
            print json.dumps(response, indent=2)
        else:
            print("Bad file: ", fileName)

        #if val:
        #else:
        #    rename(join(PATH,fileName), join(PATH, BAD_PATH, fileName))
if __name__ == "__main__":
    main()
