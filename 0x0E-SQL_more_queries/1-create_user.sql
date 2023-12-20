-- Create a new root user
-- Creating the user
CREATE USER IF NOT EXISTS "user_0d_1"@"localhost"
IDENTIFIED BY "user_0d_1_pwd";

-- Give the user all the permissions
GRANT ALL ON *.*
   TO "user_0d_1"@"localhost"
