SELECT
    extracurricular_activities,
    AVG(exam_score) AS avg_score
FROM
    students
{where_clause}
GROUP BY
    extracurricular_activities
ORDER BY
    avg_score DESC;