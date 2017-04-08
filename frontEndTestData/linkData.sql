SELECT eh1.pk,eh2.pk,DATEDIFF(GREATEST(eh1.date_to,eh2.date_to),LEAST(eh1.date_from,eh2.date_from)) strength
FROM sampleEmployeesHist eh1, sampleEmployeesHist eh2
WHERE eh1.job_name = eh2.job_name
AND eh1.pk != eh2.pk
AND (ABS(DATEDIFF(eh1.date_from,eh2.date_from)) < 1
	or ABS(DATEDIFF(eh1.date_to,eh2.date_to)) < 1)
GROUP BY eh2.pk,eh1.pk,strength