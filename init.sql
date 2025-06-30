CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

CREATE TABLE IF NOT EXISTS user_interest (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    user_name VARCHAR(50),
    product VARCHAR(50),
    viewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
s