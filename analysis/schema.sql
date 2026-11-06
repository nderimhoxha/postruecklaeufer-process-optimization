CREATE DATABASE postrueckl;
USE postrueckl;

CREATE TABLE cases (
    case_id INT AUTO_INCREMENT PRIMARY KEY,
    eligible TINYINT,
    outcome VARCHAR(20),
    cost DECIMAL(6,2),
    fee DECIMAL(6,2),
    redundant TINYINT,
    process VARCHAR(10)
);