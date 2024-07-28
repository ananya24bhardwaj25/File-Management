-- Calculate the size of each directory
WITH RECURSIVE DirectorySizes AS (
    SELECT 
        d.directory_id,
        d.name AS directory_name,
        f.size AS file_size
    FROM 
        Directories d
    LEFT JOIN 
        Files f ON d.directory_id = f.directory_id

    UNION ALL

    SELECT 
        d.directory_id,
        d.name AS directory_name,
        ds.file_size
    FROM 
        DirectorySizes ds
    JOIN 
        Directories d ON ds.directory_id = d.parent_directory_id
)
SELECT 
    d.directory_id,
    d.name AS directory_name,
    COALESCE(SUM(ds.file_size), 0) AS total_size
FROM 
    Directories d
LEFT JOIN 
    DirectorySizes ds ON d.directory_id = ds.directory_id
GROUP BY 
    d.directory_id, d.name;
