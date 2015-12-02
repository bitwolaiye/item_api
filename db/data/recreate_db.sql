drop database item_api;
create database item_api;
\c item_api;
\i models/migration/init20151202.sql
\i models/data/init_data.sql