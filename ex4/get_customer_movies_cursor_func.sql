
DECLARE
    movie_cursor REFCURSOR := 'customer_movies';
    v_profile_count INTEGER;
BEGIN
    -- Check if customer exists and has profiles
    SELECT COUNT(*) INTO v_profile_count
    FROM profiles 
    WHERE customer_id = p_customer_id;
    
    IF v_profile_count = 0 THEN
        RAISE EXCEPTION 'Customer % has no profiles', p_customer_id;
    END IF;
    
    OPEN movie_cursor FOR
        SELECT 
            wh.movie_id,
            SUM(wh.duration_watched) as total_minutes,
            COUNT(*) as watch_count,
            MAX(wh.watch_date) as last_watched,
            CASE WHEN f.movie_id IS NOT NULL THEN 'Yes' ELSE 'No' END as is_favorite,
            COALESCE(r.rating, 0) as rating
        FROM profiles p
        JOIN watch_history wh ON p.watch_history_id = wh.watch_history_id
        LEFT JOIN favorites f ON p.profile_id = f.profile_id AND wh.movie_id = f.movie_id
        LEFT JOIN reviews r ON p.profile_id = r.profile_id AND wh.movie_id = r.movie_id
        WHERE p.customer_id = p_customer_id
        GROUP BY wh.movie_id, f.movie_id, r.rating
        ORDER BY total_minutes DESC;
        
    RETURN movie_cursor;
EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error in get_customer_movies_cursor: %', SQLERRM;
        RETURN NULL;
END;
