CREATE TABLE Discounts
(
  discount_id INT NOT NULL,
  discount_percent INT NOT NULL,
  valid_until DATE NOT NULL,
  PRIMARY KEY (discount_id)
);

CREATE TABLE Subscription_Plans
(
  plan_id INT NOT NULL,
  country VARCHAR(40) NOT NULL,
  plan_type VARCHAR(20) NOT NULL,
  monthly_cost NUMERIC(6,2) NOT NULL,
  device_limit INT,
  PRIMARY KEY (plan_id)
);

CREATE TABLE Subscriptions
(
  subscription_id INT NOT NULL,
  customer_name VARCHAR(40),
  plan_id INT NOT NULL,
  discount_id INT NOT NULL,
  PRIMARY KEY (subscription_id),
  FOREIGN KEY (plan_id) REFERENCES Subscription_Plans(plan_id),
  FOREIGN KEY (discount_id) REFERENCES Discounts(discount_id)
);

CREATE TABLE Payments
(
  payment_id INT NOT NULL,
  amount NUMERIC(6,2)),
  payment_date DATE NOT NULL,
  subscription_id INT NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (subscription_id) REFERENCES Subscriptions(subscription_id)
);

CREATE TABLE Refunds
(
  refund_id INT NOT NULL,
  refund_amount NUMERIC(6,2) NOT NULL,
  refund_date DATE NOT NULL,
  payment_id INT NOT NULL,
  PRIMARY KEY (refund_id),
  FOREIGN KEY (payment_id) REFERENCES Payments(payment_id)
);

CREATE TABLE Transactions
(
  transaction_id INT NOT NULL,
  status VARCHAR(20) NOT NULL,
  transaction_date DATE NOT NULL,
  payment_id INT NOT NULL,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (payment_id) REFERENCES Payments(payment_id)
);