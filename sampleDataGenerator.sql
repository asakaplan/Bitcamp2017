SELECT eh1.pk,eh2.pk,DATEDIFF(GREATEST(eh1.date_to,eh2.date_to),LEAST(eh1.date_from,eh2.date_from)) test
FROM sampleEmployeesHist eh1, sampleEmployeesHist eh2
WHERE eh1.job_name = eh2.job_name
AND eh1.pk != eh2.pk
AND (ABS(DATEDIFF(eh1.date_from,eh2.date_from)) < 1
	or ABS(DATEDIFF(eh1.date_to,eh2.date_to)) < 1)
GROUP BY eh2.pk,eh1.pk,test


Error Code: 1055. Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'people.eh1.date_to' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'Error Code: 1055. Expression #3 of SELECT list is not in GROUP BY clause and con' at line 10
Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'Error Code: 1055. Expression #3 of SELECT list is not in GROUP BY clause and con' at line 10
