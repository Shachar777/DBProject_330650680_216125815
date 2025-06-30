
DECLARE
    v_movie_rec RECORD;
    v_transferred_count INTEGER := 0;
    v_from_customer INTEGER;
    v_to_customer INTEGER;
BEGIN
    -- Check if profiles exist
    SELECT customer_id INTO v_from_customer 
    FROM profiles WHERE profile_id = p_from_profile_id;
    
    SELECT customer_id INTO v_to_customer 
    FROM profiles WHERE profile_id = p_to_profile_id;
    
    IF v_from_customer IS NULL OR v_to_customer IS NULL THEN
        RAISE EXCEPTION 'Profile not found';
    END IF;
    
    -- Check customer restriction only if not allowed
    IF NOT p_allow_cross_customer AND v_from_customer != v_to_customer THEN
        RAISE EXCEPTION 'Cannot transfer between different customers';
    END IF;
    
    -- Transfer favorites
    FOR v_movie_rec IN 
        SELECT movie_id, last_seen, total_time_watched
        FROM favorites 
        WHERE profile_id = p_from_profile_id
        LIMIT p_movie_limit
    LOOP
        INSERT INTO favorites (profile_id, movie_id, last_seen, total_time_watched)
        VALUES (p_to_profile_id, v_movie_rec.movie_id, v_movie_rec.last_seen, v_movie_rec.total_time_watched)
        ON CONFLICT (profile_id, movie_id) DO NOTHING;
        
        DELETE FROM favorites 
        WHERE profile_id = p_from_profile_id 
        AND movie_id = v_movie_rec.movie_id;
        
        v_transferred_count := v_transferred_count + 1;
    END LOOP;

EXCEPTION
    WHEN OTHERS THEN
        RAISE;
END;
