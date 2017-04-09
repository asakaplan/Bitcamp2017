from sys import argv
samplePeopleRaw = [a.split(",") for a in open("frontEndTestData/person%s.csv"%argv[1],"r").readlines()[1:]]
sampleLinksRaw =  [a.split(",") for a in open("frontEndTestData/links%s.csv"%argv[1],"r").readlines()[1:]]

outp = {"nodes":[[int(a[0]),a[1].strip().replace('"', ""),a[3].strip().replace('"', ""),float(a[2]), a[4].strip().replace('"', ""), a[5].strip().replace('"', "")] for a in samplePeopleRaw],
        "links":[[*map(int,a)] for a in sampleLinksRaw]
        }

open("public/js/data.json","w").write(str(outp).replace("'",'"'))
