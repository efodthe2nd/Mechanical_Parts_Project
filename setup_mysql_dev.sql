-- this script prepares a MySQL server for the project
-- create project development database with the name : mech_dev_db
CREATE DATABASE IF NOT EXISTS mech_dev_db;
-- creating new user named : mech_dev with all privileges on the db mech_dev_db
-- with the password: mech_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'mech_dev'@'localhost' IDENTIFIED BY 'mech_dev_pwd';
-- granting all privileges to the new user
GRANT ALL PRIVILEGES ON mech_dev_db.* TO 'mech_dev'@'localhost';
FLUSH PRIVILEGES;
