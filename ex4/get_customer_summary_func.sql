
BEGIN
    RETURN QUERY
    SELECT 
        c.customer_name::VARCHAR,
        COUNT(DISTINCT p.profile_id)::INTEGER,
        COALESCE(SUM(wh.duration_watched), 0)::INTEGER,
        COUNT(DISTINCT f.movie_id)::INTEGER,
        COALESCE(AVG(r.rating), 0)::DECIMAL(4,2),
        COALESCE((SELECT py.amount FROM payments py 
         WHERE py.customer_id = p_customer_id 
         ORDER BY py.payment_date DESC LIMIT 1), 0)::DECIMAL(10,2)
    FROM customers c
    LEFT JOIN profiles p ON c.customer_id = p.customer_id
    LEFT JOIN watch_history wh ON p.watch_history_id = wh.watch_history_id
    LEFT JOIN favorites f ON p.profile_id = f.profile_id
    LEFT JOIN reviews r ON p.profile_id = r.profile_id
    WHERE c.customer_id = p_customer_id
    GROUP BY c.customer_id, c.customer_name;
END;
