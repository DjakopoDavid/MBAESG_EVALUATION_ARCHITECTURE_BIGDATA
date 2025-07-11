SELECT
    extracurricular_participation,
    AVG(exam_score) AS avg_score
FROM
    etudiants
{where_clause}
GROUP BY
    extracurricular_participation
ORDER BY
    avg_score DESC;