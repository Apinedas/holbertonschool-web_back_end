-- Calcas and stores avg score
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN
    SET @average = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
    UPDATE users SET average_score = @average WHERE id = user_id;
END $$
DELIMITER ;