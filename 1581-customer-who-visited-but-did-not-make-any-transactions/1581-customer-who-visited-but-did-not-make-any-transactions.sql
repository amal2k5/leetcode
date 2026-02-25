# Write your MySQL query statement below
SELECT v.customer_id, count(v.visit_id) as count_no_trans from Visits v 
LEFT JOIN Transactions t on t.visit_id = v.visit_id
WHERE transaction_id IS NULL 
GROUP BY customer_id;