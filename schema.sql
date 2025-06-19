CREATE DATABASE DB1;
USE DB1;
CREATE TABLE assessment(
	student_name VARCHAR(30),
    college_name VARCHAR(50),
    round1 FLOAT,
    round2 FLOAT,
    round3 FLOAT,
    tech_round FLOAT,
    total_marks FLOAT,
    result VARCHAR(10),
    place INT
);

SELECT * FROM assessment;