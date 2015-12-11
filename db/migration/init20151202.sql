CREATE TABLE items
(
  item_id    SERIAL  NOT NULL,
  item_name  TEXT    NOT NULL,
  item_desc  TEXT,
  item_price DECIMAL NOT NULL,
  PRIMARY KEY (item_id)
);

CREATE TABLE users
(
  user_id      SERIAL NOT NULL,
  user_name    TEXT,
  user_phone   TEXT,
  user_email   TEXT,
  user_address TEXT,
  PRIMARY KEY (user_id)
);

CREATE TABLE user_items
(
  user_id INTEGER NOT NULL REFERENCES users ON DELETE CASCADE,
  item_id INTEGER NOT NULL REFERENCES items ON DELETE CASCADE,
  PRIMARY KEY (user_id, item_id)
);

CREATE TABLE orders
(
  order_id   SERIAL    NOT NULL,
  user_id    INTEGER   NOT NULL REFERENCES users ON DELETE CASCADE,
  item_id    INTEGER   NOT NULL REFERENCES items ON DELETE CASCADE,
  item_price DECIMAL   NOT NULL,
  buy_time   TIMESTAMP NOT NULL,
  raw        TEXT,
  PRIMARY KEY (order_id)
);

CREATE TABLE order_stages
(
  order_id         INTEGER NOT NULL,
  order_stage_id   INTEGER NOT NULL,
  order_stage_name TEXT,
  order_stage_time TEXT,
  PRIMARY KEY (order_id, order_stage_id)
);

CREATE TABLE order_devices
(
  order_id     INTEGER NOT NULL,
  device_token TEXT    NOT NULL,
  PRIMARY KEY (order_id, device_token)
);

CREATE TABLE order_notifications
(
  order_id       INTEGER NOT NULL,
  order_stage_id INTEGER NOT NULL,
  device_token   TEXT    NOT NULL,
  push_time      TIMESTAMP,
  PRIMARY KEY (order_id, order_stage_id, device_token)
);