DROP TABLE sampleEmployees;
CREATE TABLE sampleEmployees SELECT * FROM people WHERE badness > .7 LIMIT 300;
INSERT INTO sampleEmployees SELECT * FROM people WHERE badness < .01 LIMIT 700;

DROP TABLE sampleEmployeesHist;
CREATE TABLE sampleEmployeesHist SELECT eh2.* FROM sampleEmployees e1, employmentHistory eh2 WHERE e1.pk = eh2.pk;

SELECT DISTINCT se.pk, CONCAT(first_name,' ',last_name) full_name, badness, REPLACE(seh.job_name,",",""),seh.state_name, seh.city_name
FROM sampleEmployees se, sampleEmployeesHist seh
WHERE seh.job_name = (SELECT job_name FROM sampleEmployeesHist sehInner WHERE sehInner.pk = se.pk ORDER BY date_to DESC LIMIT 1)
AND se.pk = seh.pk;

SELECT eh1.pk,eh2.pk,DATEDIFF(GREATEST(eh1.date_to,eh2.date_to),LEAST(eh1.date_from,eh2.date_from)) strength
FROM sampleEmployeesHist eh1, sampleEmployeesHist eh2
WHERE eh1.job_name = eh2.job_name
AND eh1.pk != eh2.pk
AND (ABS(DATEDIFF(eh1.date_from,eh2.date_from)) < 1
	or ABS(DATEDIFF(eh1.date_to,eh2.date_to)) < 1)
GROUP BY eh2.pk,eh1.pk,strength;