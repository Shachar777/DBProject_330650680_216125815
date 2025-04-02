-- Disable foreign key checks to prevent errors during deletion
--SET FOREIGN_KEY_CHECKS = 0;

-- Drop tables in reverse order of creation to avoid dependency issues
DROP TABLE IF EXISTS Refunds CASCADE;
DROP TABLE IF EXISTS Transactions CASCADE;
DROP TABLE IF EXISTS Payments CASCADE;
DROP TABLE IF EXISTS Subscriptions CASCADE;
DROP TABLE IF EXISTS Discounts CASCADE;
DROP TABLE IF EXISTS Subscription_Plans CASCADE;

-- Re-enable foreign key checks
--SET FOREIGN_KEY_CHECKS = 1;
