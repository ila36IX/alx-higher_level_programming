
-- creates the database hbtn_0d_usa and the table cities 
-- create the datebase if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- change the dataase
USE hbtn_0d_usa;

-- Create the table state
CREATE TABLE IF NOT EXISTS cities(
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id),
          id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT                       NOT NULL,
        name VARCHAR(256)              NOT NULL
);
