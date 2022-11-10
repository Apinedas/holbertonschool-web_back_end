-- Calcas and stores avg score
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(arg_id int)
BEGIN
    SET @average = (SELECT AVG(score) FROM corrections GROUP BY user_id HAVING user_id = arg_id);
    UPDATE users SET average_score = @average WHERE id = arg_id;
END $$
DELIMITER ;