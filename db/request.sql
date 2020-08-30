SELECT
 j.date,
 j.status,
 COUNT(j.uid),
 SUM(j.duration) AS cuple_duration,
 p.name,
 s.name
FROM journal AS j
JOIN project AS p ON p.id = j.project_id
JOIN server AS s ON s.id = j.server_id
WHERE j.date BETWEEN '2020-08-25' AND '2020-09-01'
GROUP BY j.status, p.name, s.name, j.date
