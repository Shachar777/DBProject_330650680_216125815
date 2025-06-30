-- main_program_2.sql
DO $$
DECLARE
    v_customer_id INTEGER := 8;
    v_from_profile INTEGER := 8;
    v_to_profile INTEGER := 7;
    v_movies_limit INTEGER := 3;
    
    -- משתנים לעבודה עם cursor
    movies_cursor REFCURSOR;
    v_movie_record RECORD;
    v_movie_count INTEGER := 0;
    
    -- משתנים כלליים
    v_start_time TIMESTAMP;
    v_program_name VARCHAR(50) := 'Profile Management Program';
BEGIN
    v_start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '=== % Started at % ===', v_program_name, v_start_time;
    
    -- חלק 1: קבלת רשימת סרטים עם cursor
    RAISE NOTICE 'Step 1: Getting customer movies with cursor...';
    
    movies_cursor := get_customer_movies_cursor(v_customer_id);
    
    -- קריאה מה-cursor
    LOOP
        FETCH movies_cursor INTO v_movie_record;
        EXIT WHEN NOT FOUND;
        
        v_movie_count := v_movie_count + 1;
        
        -- הדפס רק 3 סרטים ראשונים
        IF v_movie_count <= 3 THEN
            RAISE NOTICE 'Movie %: ID=%, Minutes=%, Favorite=%', 
                         v_movie_count,
                         v_movie_record.movie_id,
                         v_movie_record.total_minutes,
                         v_movie_record.is_favorite;
        END IF;
    END LOOP;
    
    CLOSE movies_cursor;
    RAISE NOTICE 'Found % movies total', v_movie_count;
    
    -- חלק 2: העברת מועדפים בין פרופילים
    RAISE NOTICE 'Step 2: Transferring favorites between profiles...';
    
    CALL transfer_favorites(v_from_profile, v_to_profile, v_movies_limit, true);
    
    RAISE NOTICE 'Favorites transferred successfully!';
    
    -- סיכום התוכנית
    RAISE NOTICE '=== % Completed in % seconds ===', 
                 v_program_name,
                 EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - v_start_time));

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'ERROR in %: %', v_program_name, SQLERRM;
END $$;