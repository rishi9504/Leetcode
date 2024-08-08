# Write your MySQL query statement below

with  cte as  (
    select e.name as ename, d.name as dname,salary,dense_rank() over(partition by departmentId order by salary desc) as rnk from employee e join department d on e.departmentId = d.id
)
select cte.dname Department ,ename Employee , salary Salary from cte where rnk<4
