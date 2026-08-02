-- Write your query below

-- select name from customers where id not in (select customer_id from orders);
select name from customers 

except 

select customers.name from customers 
inner join orders on customers.id = orders.customer_id