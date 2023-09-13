-- Drop Table if it exists
DROP TABLE IF EXISTS persons;

-- Create the persons schema
CREATE TABLE persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at DATETIME NOT NULL,
    name VARCHAR(60) NOT NULL,
    age INTEGER,
    phone VARCHAR(20),
    email VARCHAR(60)
);
