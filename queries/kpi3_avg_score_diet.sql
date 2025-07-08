SELECT
    diet_quality,
    AVG(exam_score) AS avg_score
FROM
    students
{where_clause}
GROUP BY
    diet_quality
ORDER BY
    avg_score DESC;