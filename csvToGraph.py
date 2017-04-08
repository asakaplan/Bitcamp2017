samplePeopleRaw = [a.split(",") for a in open("frontEndTestData/samplePeople.csv","r")]
sampleLinksRaw =  [a.split(",") for a in open("frontEndTestData/sampleLinks.csv","r")]

outp = {"nodes":[[int(a[0]),a[1].strip()[1:-1],a[3].strip()[1:-1],float(a[2])] for a in samplePeopleRaw],
        "links":[[*map(int,a)] for a in sampleLinksRaw]
        }
print(outp)