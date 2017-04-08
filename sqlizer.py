import pickle
from mysql.connector import (connection)
bigTableName = "people"
pk, lastName, firstName, flags = "pk","last_name","first_name","flags"
bigTableStatement = """CREATE TABLE IF NOT EXISTS `%s` (
    `%s` int,
    `%s` varchar(32) NOT NULL,
    `%s` varchar(32) NOT NULL,
    `%s` int NOT NULL,
    PRIMARY KEY (`%s`)
);
"""%(bigTableName, pk, lastName, firstName, flags, pk)
jobName, cityName, stateName, dateFrom, dateTo = "job_name", "city_name", "state_name", "date_from","date_to"

employeeHistoryTableName = "employmentHistory"
employeeHistoryStatement = """CREATE TABLE IF NOT EXISTS `%s` (
 `%s` int,
 `%s` varchar(64) NOT NULL,
 `%s` varchar(32) NOT NULL,
 `%s` varchar(2) NOT NULL,
 `%s` date NOT NULL,
 `%s` date NOT NULL,
 PRIMARY KEY (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`),
 FOREIGN KEY (`%s`) REFERENCES `%s` (`%s`)

);
"""%(employeeHistoryTableName, pk, jobName, cityName, stateName, dateFrom, dateTo, pk, jobName, cityName, stateName, dateFrom,dateTo, pk, bigTableName, pk)
cnx = connection.MySQLConnection(user="root", password="fuck", database='people')
cursor = cnx.cursor()

cursor.execute(bigTableStatement)
cursor.execute(employeeHistoryStatement)

a=pickle.load(open("consolodatedOutput.pic","r"))
print "Loaded data"

for person in a:
    name, employment,flags = person
    flagBin = 0
    for i in flags:
        flagBin <<=1
        flagBin += i
    #print "INSERT INTO %s VALUES (%d, `%s`, `%s`, %d);"%(bigTableName, name[2],name[0].replace("'",""),name[1].replace("'",""),flagBin)
    cursor.execute("INSERT INTO %s VALUES (%d, '%s', '%s', %d);"%(bigTableName, name[2],name[0].replace("'",""),name[1].replace("'",""),flagBin))
    for place in employment:
        #print "INSERT INTO %s VALUES (%d, '%s', '%s', '%s', STR_TO_DATE('%s','%%m/%%Y'), STR_TO_DATE(''%s,'%%m/%%Y'));"%(employeeHistoryTableName, name[2],place[0][0],place[0][1],place[0][2], place[1][0],place[1][1])
        try:
            cursor.execute("INSERT INTO %s VALUES (%d, '%s', '%s', '%s', STR_TO_DATE('01/%s','%%d/%%m/%%Y'), STR_TO_DATE('01/%s','%%d/%%m/%%Y'));"%(employeeHistoryTableName, name[2],place[0][0].replace("'",""),place[0][1],place[0][2], place[1][0],place[1][1]))
        except Exception as e:
            print "Yo we dun goffed ", e
cnx.commit()
cursor.close()
cnx.close()
