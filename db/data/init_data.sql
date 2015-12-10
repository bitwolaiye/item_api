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

COMMIT;