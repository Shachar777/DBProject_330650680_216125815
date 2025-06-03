ALTER TABLE Customers RENAME COLUMN subscription_id TO customer_id
ALTER TABLE customers add COLUMN date_of_birth DATE
ALTER TABLE customers add COLUMN customer_since DATE
ALTER TABLE payments ADD COLUMN currency VARCHAR(40)
ALTER TABLE payments ADD COLUMN payment_method VARCHAR(40)
DROP TABLE mark_as_favorite
DROP TABLE payment
DROP TABLE devices
DROP TABLE customer
ALTER TABLE profiles RENAME COLUMN profilename TO profile_name
ALTER TABLE profiles RENAME COLUMN customerid TO customer_id
ALTER TABLE profiles RENAME COLUMN watchhistoryid TO watch_history_id
ALTER TABLE profiles RENAME COLUMN isonline TO is_online
ALTER TABLE profiles RENAME COLUMN profilepicture TO profile_picture
ALTER TABLE reviews RENAME COLUMN movieid TO movie_id
ALTER TABLE watch_history RENAME COLUMN watchhistoryid TO watch_history_id
ALTER TABLE watch_history RENAME COLUMN durationwatched TO duration_watched
ALTER TABLE watch_history RENAME COLUMN movieid TO movie_id
ALTER TABLE watch_history RENAME COLUMN watchdate TO watch_date

ALTER TABLE favorites
ADD CONSTRAINT favorites_profileid_fkey
FOREIGN KEY (profile_id)
REFERENCES profiles (profile_id);