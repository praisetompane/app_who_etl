SELECT * FROM public.alembic_version

SELECT * FROM INFORMATION_SCHEMA.TABLES;


-- Retrive all ETL runs

SELECT * FROM etl.etl;

-- Retreive annualconfirmedcases for a specific ETL run
SELECT * FROM malaria.annualconfirmedcases ac
INNER JOIN etl.etl e ON ac.etl_id  = e.id
WHERE e.id = 44

-- Retrieve all whogho malaria annual confirmed cases
SELECT * FROM sourcedata.whoghomalariaannualconfirmedcases