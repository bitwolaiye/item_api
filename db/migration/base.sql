CREATE database item_api;
CREATE USER item_api WITH PASSWORD 'item_api';
ALTER USER item_api CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE "item_api" to item_api;