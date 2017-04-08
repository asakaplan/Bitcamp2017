SELECT eh1.pk, eh2.pk
FROM employmentHistory eh2, 
(SELECT DISTINCT *
	FROM employmentHistory ehInner
	LIMIT 40) 
AS eh1
WHERE eh1.job_name = eh2.job_name
AND eh1.pk != eh2.pk
AND (ABS(DATEDIFF(eh1.date_from,eh2.date_from)) < 1
	OR ABS(DATEDIFF(eh1.date_to,eh2.date_to)) < 1)
AND eh1.pk IN (
SELECT eh2.pk
FROM employmentHistory eh2, 
(SELECT DISTINCT *
	FROM employmentHistory ehInner
	LIMIT 40) 
AS eh1
WHERE eh1.job_name = eh2.job_name
AND eh1.pk != eh2.pk
AND (ABS(DATEDIFF(eh1.date_from,eh2.date_from)) < 1
	OR ABS(DATEDIFF(eh1.date_to,eh2.date_to)) < 1)
GROUP BY eh2.pk HAVING COUNT(eh2.pk) < 5)
GROUP BY eh1.pk, eh2.pk; 

DROP TABLE sampleEmployeesHist
CREATE TABLE sampleEmployeesHist SELECT eh2.* FROM sampleEmployees e1, employmentHistory eh2 WHERE e1.pk = eh2.pk

DROP TABLE sampleEmployees
CREATE TABLE sampleEmployees SELECT * FROM people WHERE badness > .7 LIMIT 1000
INSERT INTO sampleEmployees SELECT * FROM people WHERE badness < .01 LIMIT 1000

SELECT badness, COUNT(badness) FROM people GROUP BY badness LIMIT 1000