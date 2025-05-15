curl  -X POST --location 'http://localhost:8080/app_who_etl/api/etl/' \
--header 'Content-Type: application/json' \
--data '
    {
        "etl_name": "Malaria Annual Confirmed Cases"
    }
'
