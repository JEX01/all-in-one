-- Database: `dailyexpense`
CREATE DATABASE dailyexpense;
use dailyexpense;
DROP DATABASE dailyexpense;

-- Table structure for table `expenses`
CREATE TABLE `expenses` (
  `expense_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(15) NOT NULL,
  `expense` int(20) NOT NULL,
  `expensedate` varchar(15) NOT NULL,
  `expensecategory` varchar(50) NOT NULL,
  PRIMARY KEY (`expense_id`)
);

-- Table structure for table `expense_categories`
CREATE TABLE `expense_categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) NOT NULL,
  PRIMARY KEY (`category_id`)
);

-- Table structure for table `users`
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
);

delete from users;

select  * from users;
select * from expenses;
select * from expense_categories;