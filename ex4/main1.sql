-- main_program_1.sql
DO $$
DECLARE
    v_customer_id INTEGER := 1;
    v_new_plan_id INTEGER := 2;
    v_discount_percent INTEGER := 15;
    
    -- משתנים לפונקציה
    v_summary_record RECORD;
    
    -- משתנים כלליים
    v_start_time TIMESTAMP;
    v_program_name VARCHAR(50) := 'Customer Analysis Program';
BEGIN
    v_start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '=== % Started at % ===', v_program_name, v_start_time;
    
    -- חלק 1: קבלת סיכום לקוח עם הפונקציה
    RAISE NOTICE 'Step 1: Getting customer summary...';
    
    SELECT * INTO v_summary_record
    FROM get_customer_summary(v_customer_id);
    
    RAISE NOTICE 'Customer: %, Profiles: %, Watch Minutes: %, Favorites: %', 
                 v_summary_record.customer_name,
                 v_summary_record.total_profiles,
                 v_summary_record.total_watch_minutes,
                 v_summary_record.favorite_count;
    
    -- חלק 2: עדכון מנוי עם הפרוצדורה
    RAISE NOTICE 'Step 2: Updating customer subscription...';
    
    CALL update_customer_subscription(v_customer_id, v_new_plan_id, v_discount_percent);
    
    RAISE NOTICE 'Subscription updated successfully!';
    
    -- סיכום התוכנית
    RAISE NOTICE '=== % Completed in % seconds ===', 
                 v_program_name, 
                 EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - v_start_time));

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'ERROR in %: %', v_program_name, SQLERRM;
END $$;