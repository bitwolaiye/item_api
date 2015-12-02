drop database item_api;
create database item_api;
\c item_api;
\i db/migration/init20151202.sql
\i db/data/init_data.sql