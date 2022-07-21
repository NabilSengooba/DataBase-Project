
CREATE DATABASE Sneakers;

CREATE TABLE `customers` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `email` text,
  `name` text
);

CREATE TABLE `Sneaker_brand` (
  `sneaker_id` int PRIMARY KEY AUTO_INCREMENT,
  `brand_name` text,
  `price` int
);

CREATE TABLE `Category` (
  `Cat_id` int PRIMARY KEY AUTO_INCREMENT,
  `size` int,
  `colour` int
);

CREATE TABLE `Cart_item` (
  `cart_id` int PRIMARY KEY AUTO_INCREMENT,
  `quantity` int,
  `total_cost` int
);

CREATE TABLE `Payment` (
  `payment_id` int PRIMARY KEY AUTO_INCREMENT,
  `payment_type` text,
  `total_cost` int
);

CREATE TABLE `Purchase_Details` (
  `pd_id` int PRIMARY KEY AUTO_INCREMENT,
  `id` int,
  `sneaker_id` int,
  `Cat_id` int,
  `cart_id` int,
  `payment_id` int,
  `location` text
);

ALTER TABLE `Purchase_Details` ADD FOREIGN KEY (`id`) REFERENCES `customers` (`id`);

ALTER TABLE `Purchase_Details` ADD FOREIGN KEY (`sneaker_id`) REFERENCES `Sneaker_brand` (`sneaker_id`);

ALTER TABLE `Purchase_Details` ADD FOREIGN KEY (`Cat_id`) REFERENCES `Category` (`Cat_id`);

ALTER TABLE `Purchase_Details` ADD FOREIGN KEY (`cart_id`) REFERENCES `Cart_item` (`cart_id`);

ALTER TABLE `Purchase_Details` ADD FOREIGN KEY (`payment_id`) REFERENCES `Payment` (`payment_id`);
