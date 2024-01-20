CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE new_database;
GRANT ALL PRIVILEGES ON new_database.* TO 'new_user'@'localhost';
FLUSH PRIVILEGES;



USE new_database;

CREATE TABLE user (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    sex VARCHAR(10),
    age INT,
    phone VARCHAR(20)
);

INSERT INTO user (id, name, sex, age, phone)
VALUES (1, '张美比', 'Female', 25, '123-456-7890'),
       (2, '苏帅比', 'Male', 30, '987-654-3210'),
       (3, '李帅比', 'Male', 22, '555-123-4567');





SELECT * FROM user WHERE age BETWEEN 20 AND 30;





DELETE FROM user WHERE name LIKE '%张%';





SELECT AVG(age) FROM user;





SELECT * FROM user WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%' ORDER BY age DESC;





CREATE TABLE team (
    id INT PRIMARY KEY,
    teamName VARCHAR(255)
);

CREATE TABLE score (
    id INT PRIMARY KEY,
    teamid INT,
    userid INT,
    score INT,
    FOREIGN KEY (teamid) REFERENCES team(id),
    FOREIGN KEY (userid) REFERENCES user(id)
);



SELECT u.* FROM user u
JOIN score s ON u.id = s.userid
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU' AND u.age < 20;





SELECT t.teamName, COALESCE(SUM(s.score), 0) AS total_score
FROM team t
LEFT JOIN score s ON t.id = s.teamid
WHERE t.teamName = 'ECNU'
GROUP BY t.teamName;