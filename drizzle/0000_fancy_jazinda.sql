CREATE TABLE `ai_cache` (
	`key` text PRIMARY KEY NOT NULL,
	`response` text NOT NULL,
	`created_at` integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE `ai_usage` (
	`user_id` text NOT NULL,
	`minute` integer NOT NULL,
	`count` integer DEFAULT 0 NOT NULL,
	PRIMARY KEY(`user_id`, `minute`)
);
--> statement-breakpoint
CREATE TABLE `assets` (
	`id` text PRIMARY KEY NOT NULL,
	`key` text NOT NULL,
	`name` text NOT NULL,
	`content_type` text NOT NULL,
	`size` integer NOT NULL,
	`created_at` integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE `attempts` (
	`id` text PRIMARY KEY NOT NULL,
	`user_id` text NOT NULL,
	`unit_id` text NOT NULL,
	`word_id` text NOT NULL,
	`mode` text NOT NULL,
	`answer` text NOT NULL,
	`correct` integer NOT NULL,
	`assisted` integer DEFAULT false NOT NULL,
	`created_at` integer NOT NULL,
	`seconds` integer NOT NULL,
	`rating` text
);
--> statement-breakpoint
CREATE INDEX `attempt_user` ON `attempts` (`user_id`,`created_at`);--> statement-breakpoint
CREATE TABLE `books` (
	`id` text PRIMARY KEY NOT NULL,
	`document` text NOT NULL,
	`updated_at` integer NOT NULL
);
--> statement-breakpoint
CREATE TABLE `memberships` (
	`user_id` text PRIMARY KEY NOT NULL,
	`plan` text DEFAULT 'free' NOT NULL,
	`expires_at` integer
);
--> statement-breakpoint
CREATE TABLE `notes` (
	`user_id` text NOT NULL,
	`book_id` text NOT NULL,
	`page` integer NOT NULL,
	`document` text NOT NULL,
	`version` integer DEFAULT 1 NOT NULL,
	`updated_at` integer NOT NULL,
	PRIMARY KEY(`user_id`, `book_id`, `page`)
);
--> statement-breakpoint
CREATE TABLE `profiles` (
	`user_id` text PRIMARY KEY NOT NULL,
	`display_name` text DEFAULT '' NOT NULL,
	`daily_goal` integer DEFAULT 20 NOT NULL,
	`trial_started_at` integer NOT NULL,
	`last_book` text DEFAULT '' NOT NULL,
	`last_unit` text DEFAULT '' NOT NULL,
	`last_page` integer DEFAULT 1 NOT NULL
);
--> statement-breakpoint
CREATE TABLE `read_pages` (
	`user_id` text NOT NULL,
	`key` text NOT NULL,
	PRIMARY KEY(`user_id`, `key`)
);
--> statement-breakpoint
CREATE TABLE `reviews` (
	`user_id` text NOT NULL,
	`unit_id` text NOT NULL,
	`word_id` text NOT NULL,
	`due_at` integer NOT NULL,
	`stage` integer NOT NULL,
	`unknown` integer NOT NULL,
	PRIMARY KEY(`user_id`, `unit_id`, `word_id`)
);
--> statement-breakpoint
CREATE TABLE `saved_words` (
	`user_id` text NOT NULL,
	`key` text NOT NULL,
	PRIMARY KEY(`user_id`, `key`)
);
