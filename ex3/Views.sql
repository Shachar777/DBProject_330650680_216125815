CREATE VIEW subscription_planner AS
SELECT 
    c.customer_since,
	c.date_of_birth,
    sp.monthly_cost,
	sp.country,
	sp.device_limit,
	sp.plan_type,
	sp.plan_id
FROM 
    customers c
JOIN 
    subscription_plans sp ON c.plan_id = sp.plan_id;


CREATE VIEW profile_view AS
SELECT
    wh.watch_date,
    wh.movie_id AS watched_movie_id,
    wh.duration_watched,
    p.profile_name,
    p.is_online,
    f.last_seen,
    f.movie_id AS favorite_movie_id,
    f.total_time_watched
FROM
    profiles p
JOIN
    watch_history wh ON p.watch_history_id = wh.watch_history_id
JOIN
    favorites f ON p.profile_id = f.profile_id;




SELECT 
    profile_name,
    total_time_watched
FROM 
    profile_view
WHERE 
    is_online = TRUE
ORDER BY 
    watch_date DESC;



SELECT 
    profile_name,
    total_time_watched,
    favorite_movie_id,
    last_seen
FROM 
    profile_view
GROUP BY 
    profile_name, total_time_watched, favorite_movie_id, last_seen
ORDER BY 
    total_time_watched DESC
LIMIT 40;



SELECT 
    customer_since,
    date_of_birth,
    device_limit,
    monthly_cost,
    plan_type
FROM 
    subscription_planner
WHERE 
    customer_since <= '2005-01-01'
ORDER BY 
    customer_since;



SELECT 
    ROUND(monthly_cost / device_limit, 2) AS devices_cost_rate,
    customer_since,
    date_of_birth,
	device_limit,
	plan_id
FROM 
    subscription_planner
ORDER BY devices_cost_rate ASC
LIMIT 100

