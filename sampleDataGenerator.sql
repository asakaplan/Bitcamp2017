SELECT eh1.pk,eh2.pk FROM sampleEmployeesHist eh1, sampleEmployeesHist eh2
WHERE eh1.job_name = eh2.job_name
AND eh1.pk != eh2.pk
AND (ABS(DATEDIFF(eh1.date_from,eh2.date_from)) < 1
	or ABS(DATEDIFF(eh1.date_to,eh2.date_to)) < 1)
    
GROUP BY eh2.pk,eh1.pk


DELETE FROM sampleEmployeesHist
WHERE pk = pk
LIMIT 70
Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.
Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.
Error Code: 1146. Table 'people.sampleEmployeeHist' doesn't exist
