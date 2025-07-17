-- some queries
select * from expenses e join expense_categories ex_C on e.expensecategory = ex_c.category_name 
where user_id = 9 and category_id = 1;

select * from expenses ex where user_id = 9 AND expense < 400;

select * from users;

-- no of orders
select count(user_id) occ_of_user, user_id from expenses group by (user_id);

SELECT user_id, expensecategory , COUNT(*) as category_count
FROM expenses
GROUP BY user_id, expensecategory;


-- sum of expenses per user 
select user_id, sum(expense) from expenses group by user_id ;

-- max, min, avg
select max(expense), user_id as user from expenses group by user_id ;
select min(expense), user_id user from expenses group by user_id ;
select avg(expense), user_id user from expenses group by user_id ;

-- total per category
select sum(expense), user_id user from expenses group by expensecategory, user_id ;

-- recent 5 orders 
select user_id,expense, expensedate, expensecategory from expenses order by expensedate desc limit 5; 

-- user who never expense

select u.user_id from users u left join expenses exp  on u.user_id = exp.user_id
where exp.user_id is null ;

SELECT u.user_id FROM users u LEFT JOIN expenses exp ON u.user_id = exp.user_id
WHERE exp.expense_id IS NULL;

