BEGIN;
INSERT INTO items (item_name, item_desc, item_price) VALUES ('牙刷', '', 5.00);
INSERT INTO items (item_name, item_desc, item_price) VALUES ('牙膏', '', 12.00);
INSERT INTO items (item_name, item_desc, item_price) VALUES ('洗发水', '', 20.00);
INSERT INTO items (item_name, item_desc, item_price) VALUES ('护发素', '', 30.00);
INSERT INTO items (item_name, item_desc, item_price) VALUES ('面霜', '', 40.00);

INSERT INTO users (user_name) VALUES ('first');

INSERT INTO user_items (user_id, item_id) VALUES (1, 1);
INSERT INTO user_items (user_id, item_id) VALUES (1, 2);
INSERT INTO user_items (user_id, item_id) VALUES (1, 3);
INSERT INTO user_items (user_id, item_id) VALUES (1, 4);
INSERT INTO user_items (user_id, item_id) VALUES (1, 5);

INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 1, now() - interval '3 day');
INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 1, now() - interval '2 day');

INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 2, now() - interval '2 day');
INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 2, now() - interval '1 day');

INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 3, now() - interval '7 day');

INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 4, now() - interval '4 day');

INSERT INTO item_buy_histories(user_id, item_id, buy_time) VALUES (1, 5, now() - interval '1 day');

COMMIT;