# SQL Queries

## Database Schema

### Job Table
- `id` - Primary key
- `url` - Job URL
- `location` - Job location
- `salary` - Job salary

### Job_text Table
- `id_job` - Foreign key to Job.id
- `description` - Job description

## Primary Query

```sql
SELECT j.url, jt.description
FROM Job j
INNER JOIN Job_text jt ON j.id = jt.id_job
WHERE j.location IN ('Киев', 'Львов', 'Київ', 'Львів');
```

## Alternative Queries

### Partial Match Search
```sql
SELECT j.url, jt.description
FROM Job j
INNER JOIN Job_text jt ON j.id = jt.id_job
WHERE j.location LIKE '%Киев%' 
   OR j.location LIKE '%Львов%'
   OR j.location LIKE '%Київ%'
   OR j.location LIKE '%Львів%';
```

### Case-Insensitive Search (PostgreSQL)
```sql
SELECT j.url, jt.description
FROM Job j
INNER JOIN Job_text jt ON j.id = jt.id_job
WHERE LOWER(j.location) IN ('киев', 'львов', 'київ', 'львів');
```

### Case-Insensitive Search (SQL Server)
```sql
SELECT j.url, jt.description
FROM Job j
INNER JOIN Job_text jt ON j.id = jt.id_job
WHERE UPPER(j.location) IN ('КИЕВ', 'ЛЬВОВ', 'КИЇВ', 'ЛЬВІВ');
```

## Recommendations

- Use primary query for best performance
- Primary query supports both Ukrainian and Russian city names
- INNER JOIN ensures only jobs with descriptions are returned
- Consider indexing the location column for better performance

