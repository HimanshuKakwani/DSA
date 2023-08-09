# Write your MySQL query statement below
SELECT e.employee_id, e.department_id
FROM Employee e
WHERE e.primary_flag = 'Y'

UNION
SELECT e.employee_id, e.department_id
FROM Employee e
WHERE e.employee_id NOT IN(
    SELECT e.employee_id
    FROM Employee e
    WHERE e.primary_flag = 'Y'
)
group by employee_id
having count(*)=1
ORDER BY employee_id