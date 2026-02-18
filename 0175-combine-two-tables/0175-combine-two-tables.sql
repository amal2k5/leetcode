select p.lastname,p.firstName,a.city,a.state
from Person p
left join Address a on
a.personId = p.personId 