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

CREATE TABLE item_buy_histories
(
  buy_history_id SERIAL    NOT NULL,
  user_id        INTEGER   NOT NULL REFERENCES users ON DELETE CASCADE,
  item_id        INTEGER   NOT NULL REFERENCES items ON DELETE CASCADE,
  item_price     DECIMAL   NOT NULL,
  buy_time       TIMESTAMP NOT NULL,
  raw            TEXT,
  PRIMARY KEY (buy_history_id)
);

CREATE TABLE item_buy_history_steps
(
  buy_history_id        INTEGER NOT NULL,
  buy_history_step_id   INTEGER NOT NULL,
  buy_history_step      TEXT,
  buy_history_step_time TEXT,
  PRIMARY KEY (buy_history_id, buy_history_step_id)
);

CREATE TABLE item_buy_history_devices
(
  buy_history_id INTEGER NOT NULL,
  device_token   TEXT    NOT NULL,
  PRIMARY KEY (buy_history_id, device_token)
);

CREATE TABLE item_buy_history_notifications
(
  buy_history_id      INTEGER NOT NULL,
  buy_history_step_id INTEGER NOT NULL,
  device_token        TEXT    NOT NULL,
  push_time           TIMESTAMP,
  PRIMARY KEY (buy_history_id, buy_history_step_id, device_token)
);