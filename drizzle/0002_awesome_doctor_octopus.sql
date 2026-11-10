CREATE TABLE `saved_selections` (
	`user_id` text NOT NULL,
	`id` text NOT NULL,
	`document` text NOT NULL,
	`created_at` integer NOT NULL,
	PRIMARY KEY(`user_id`, `id`)
);
