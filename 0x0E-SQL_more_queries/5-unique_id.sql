-- Task5
-- comment
CREATE TABLE IF NOT EXISTS `unique_id` (
		`id` INT DEFAULT 1,
		UNIQUE(`id`),
		`name` VARCHAR(256)
);
