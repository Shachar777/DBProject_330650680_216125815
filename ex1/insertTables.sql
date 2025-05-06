-- Insert into Discounts
INSERT INTO Discounts (discount_id, discount_percent, valid_until) VALUES
(1, 10, '2025-12-31'),
(2, 20, '2025-06-30'),
(3, 15, '2025-04-15');

-- Insert into Subscription_Plans
INSERT INTO Subscription_Plans (plan_id, country, plan_type, monthly_cost, device_limit) VALUES
(1, 'Uruguay', 'standard', 10.04, 5),
(2, 'Chile', 'student', 2.46, 1),
(3, 'Uzbekistan', 'standard', 11.8, 6);

-- Insert into Subscriptions
INSERT INTO Subscriptions (subscription_id, customer_name, plan_id, discount_id) VALUES
(1, 'Alice Johnson', 1, 1),
(2, 'Bob Smith', 2, 2),
(3, 'Charlie Davis', 3, 3);

-- Insert into Payments
INSERT INTO Payments (payment_id, amount, payment_date, subscription_id) VALUES
(1, 9.99, '2025-03-01', 1),
(2, 14.99, '2025-03-02', 2),
(3, 19.99, '2025-03-03', 3);

-- Insert into Refunds
INSERT INTO Refunds (refund_id, refund_amount, refund_date, payment_id) VALUES
(1, 9.99, '2025-03-05', 1),
(2, 14.99, '2025-03-06', 2),
(3, 19.99, '2025-03-07', 3);

-- Insert into Transactions
INSERT INTO Transactions (transaction_id, status, transaction_date, payment_id) VALUES
(1, 'Success', '2025-03-01', 1),
(2, 'Failed', '2025-03-02', 2),
(3, 'Pending', '2025-03-03', 3);
