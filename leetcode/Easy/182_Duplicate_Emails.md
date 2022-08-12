**MYSQL**

```sql
select Email
from Person
group by Email
having count(*) > 1
/*
-- 내가 작성한 것.
SELECT distinct p.Email 
FROM Person p, Person p2
WHERE p.Id <> p2.Id and p.Email = p2.Email 
*/

```