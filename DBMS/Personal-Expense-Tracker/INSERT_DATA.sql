
-- Sample data for `expenses`
INSERT INTO `expenses` (`expense_id`, `user_id`, `expense`, `expensedate`, `expensecategory`) VALUES
(101, '9', 789, '2023-08-31', 'Medicine'),
(102, '9', 3, '2023-08-31', 'Entertainment'),
(103, '9', 469, '2023-08-29', 'Clothings'),
(104, '9', 985, '2023-08-25', 'Entertainment'),
(105, '12', 3, '2023-08-31', 'Clothings'),
(106, '12', 89, '2023-08-16', 'Bills & Recharges'),
(107, '9', 3, '2023-09-06', 'Clothings'),
(108, '9', 300, '2023-07-04', 'Food'),
(109, '9', 456, '2023-09-01', 'Clothings'),
(110, '9', 3, '2023-08-28', 'Entertainment'),
(111, '9', 300, '2023-09-03', 'Clothings'),
(112, '9', 789, '2021-06-03', 'Medicine'),
(113, '9', 756, '2021-02-23', 'Entertainment'),
(114, '9', 123, '2022-09-03', 'Medicine'),
(115, '9', 256, '2021-09-07', 'Medicine'),
(116, '9', 798, '2023-09-04', 'Medicine'),
(117, '9', 45, '2023-08-28', 'Entertainment'),
(118, '9', 50, '2023-10-20', 'Medicine'),
(119, '9', 786, '2023-10-20', 'Food'),
(120, '9', 1000, '2023-10-04', 'Entertainment'),
(121, '9', 500, '2023-10-19', 'Clothings'),
(122, '9', 426, '2023-10-16', 'Household Items');


-- Sample data for `expense_categories`
INSERT INTO `expense_categories` (`category_id`, `category_name`) VALUES
(1, 'Medicine'),
(2, 'Food'),
(3, 'Bills & Recharges'),
(4, 'Entertainment'),
(5, 'Clothings'),
(6, 'Rent'),
(7, 'Household Items'),
(8, 'Others');


-- Sample data for `users`
INSERT INTO `users` (`user_id`, `firstname`, `lastname`, `email`, `password`) VALUES
(9, 'Anjalita', 'Fernandes', 'anjalita@sjec.in', 'b7161ae9080c2604adb157463312ed47'),
(12, 'Ebey', 'Joe Regi', 'ejr@sjec.in', '25d55ad283aa400af464c76d713c07ad'),
(1, 'jeet', 'jonny', 'j@.com', '232329837823798239293');
