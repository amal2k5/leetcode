select name AS Customers
from Customers

where id not in (
select customerId from Orders
where customerId is not NULL
)