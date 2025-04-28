ALTER TABLE Subscription_plans
ADD CONSTRAINT chk_device_limit CHECK (device_limit > 0 AND device_limit <= 10);

ALTER TABLE Subscriptions
ALTER COLUMN customer_name SET NOT NULL;

ALTER TABLE Payments
ADD CONSTRAINT chk_payments_amount CHECK (amount > 0 AND amount <= 9999.99);