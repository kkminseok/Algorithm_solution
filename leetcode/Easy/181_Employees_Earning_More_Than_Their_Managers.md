**MYSQL**

```sql
/*
SELECT e1.Name AS Employee
FROM Employee AS e1, Employee AS e2
WHERE e1.ManagerId = e2.Id and e1.Salary > e2.Salary;
*/

-- 조인을 사용
SELECT emp.Name Employee
FROM Employee emp INNER JOIN Employee manager
on emp.ManagerId = manager.Id
WHERE emp.Salary > manager.Salary;

```