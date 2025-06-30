
BEGIN
    -- אם נוסף תשלום חדש - הפעל את כל הפרופילים של הלקוח
    UPDATE profiles 
    SET is_online = true 
    WHERE customer_id = NEW.customer_id;
    
    RETURN NEW;
END;
