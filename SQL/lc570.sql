# Write your MySQL query statement below
# select e.name 
# from Employee e 
# where t1.a >= 5 and e.id = t1.managerId
select E1.name as name
from
(select managerId,count(managerId) as a from Employee group by managerId) as t1
cross join Employee E1 on t1.managerId = E1.id
where t1.a >= 5
#as t1
