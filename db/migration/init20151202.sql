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
  user_id SERIAL NOT NULL,
  user_name TEXT NOT NULL ,
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