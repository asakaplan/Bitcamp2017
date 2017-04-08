SELECT se.pk, CONCAT(first_name,' ',last_name) full_name, badness, seh.job_name
FROM sampleEmployees se, sampleEmployeesHist seh
WHERE seh.job_name = (SELECT job_name FROM sampleEmployeesHist sehInner WHERE sehInner.pk = se.pk ORDER BY date_to DESC LIMIT 1)
AND se.pk = seh.pk