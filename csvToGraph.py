samplePeopleRaw = [a.split(",") for a in open("frontEndTestData/samplePeople.csv","r")]
sampleLinksRaw =  [a.split(",") for a in open("frontEndTestData/sampleLinks.csv","r")]

outp = {"nodes":[[int(a[0]),a[1].strip(),a[3].strip(),float(a[2])] for a in samplePeopleRaw],
        "links":[map(int,a) for a in sampleLinksRaw]
        }
print outp
