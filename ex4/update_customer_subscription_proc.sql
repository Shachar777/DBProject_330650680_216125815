
DECLARE
    v_customer_rec RECORD;
    v_old_plan_cost DECIMAL(10,2) := 0;
    v_new_plan_cost DECIMAL(10,2);
    v_final_amount DECIMAL(10,2);
    v_payment_id INTEGER;
    v_transaction_id INTEGER;
    v_next_payment_id INTEGER;
    v_next_transaction_id INTEGER;
    v_profile_rec RECORD;
    v_profile_count INTEGER := 0;
    v_old_plan_id INTEGER;
BEGIN
    -- Validate customer exists and get current plan
    SELECT customer_name, customer_since, plan_id INTO v_customer_rec
    FROM customers 
    WHERE customer_id = p_customer_id;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Customer not found';
    END IF;
    
    v_old_plan_id := v_customer_rec.plan_id;
    
    -- Get current plan cost
    SELECT COALESCE(amount, 0) INTO v_old_plan_cost
    FROM payments 
    WHERE customer_id = p_customer_id
    ORDER BY payment_date DESC
    LIMIT 1;
    
    -- Get new plan cost
    SELECT monthly_cost INTO v_new_plan_cost
    FROM subscription_plans
    WHERE plan_id = p_new_plan_id;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Plan not found';
    END IF;
    
    -- Calculate final amount with discount
    v_final_amount := v_new_plan_cost * (1 - p_discount_percent::DECIMAL / 100);
    
    -- Get next payment_id manually
    SELECT COALESCE(MAX(payment_id), 0) + 1 INTO v_next_payment_id
    FROM payments;
    
    -- Create new payment record
    INSERT INTO payments (payment_id, customer_id, payment_date, amount, payment_method, currency)
    VALUES (v_next_payment_id, p_customer_id, CURRENT_DATE, v_final_amount, 'CREDIT_CARD', 'USD')
    RETURNING payment_id INTO v_payment_id;
    
    -- Get next transaction_id manually
    SELECT COALESCE(MAX(transaction_id), 0) + 1 INTO v_next_transaction_id
    FROM transactions;
    
    -- Create transaction record
    INSERT INTO transactions (transaction_id, payment_id, transaction_date, status)
    VALUES (v_next_transaction_id, v_payment_id, CURRENT_DATE, 'COMPLETED')
    RETURNING transaction_id INTO v_transaction_id;
    
    -- Update customer's plan_id
    UPDATE customers 
    SET plan_id = p_new_plan_id
    WHERE customer_id = p_customer_id;
    
    

EXCEPTION
    WHEN OTHERS THEN
        RAISE;
END;
