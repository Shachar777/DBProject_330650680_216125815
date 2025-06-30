
DECLARE
    v_payment_count INTEGER;
    v_recent_payments INTEGER;
BEGIN
    -- בדוק תשלומים מהחודש האחרון
    SELECT COUNT(*) INTO v_recent_payments
    FROM payments 
    WHERE customer_id = OLD.customer_id
    AND payment_date >= CURRENT_DATE - INTERVAL '30 days';
    
    -- בדוק סך כל התשלומים
    SELECT COUNT(*) INTO v_payment_count
    FROM payments 
    WHERE customer_id = OLD.customer_id;
    
    -- מנע מחיקה אם יש תשלומים חדשים
    IF v_recent_payments > 0 THEN
        RAISE EXCEPTION 'Cannot delete customer - has recent payments';
    END IF;
    
    -- מנע מחיקה אם יש תשלומים בכלל
    IF v_payment_count > 0 THEN
        RAISE EXCEPTION 'Cannot delete customer - has payment history';
    END IF;
    
    -- אפשר מחיקה
    RETURN OLD;
END;
