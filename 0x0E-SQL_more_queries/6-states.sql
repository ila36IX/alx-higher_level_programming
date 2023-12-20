-- creates the database hbtn_0d_usa and the table states
-- create the datebase if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- change the dataase
USE hbtn_0d_usa;

-- Create the table state
CREATE TABLE IF NOT EXISTS states (
    PRIMARY KEY (id),
      id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256)              NOT NULL
);
