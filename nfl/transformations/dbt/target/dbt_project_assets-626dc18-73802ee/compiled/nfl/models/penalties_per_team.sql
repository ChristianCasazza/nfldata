SELECT
    penalty_team, 
    week,
    penalty_type,
    COUNT(*) AS total_penalties
FROM "nfl_database"."main"."nfl_pbp_2024"
WHERE penalty_type IS NOT NULL
GROUP BY 
    week,
    penalty_type,
    penalty_team
ORDER BY 
    week ASC