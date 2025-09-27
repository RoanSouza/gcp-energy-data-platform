CREATE OR REPLACE TABLE dataset_refined.energy_consumption AS
SELECT
  DATE(data) AS data,
  cidade,
  consumo_mwh,
  consumo_mwh * 1000 AS consumo_kwh
FROM
  dataset_trusted.energy_consumption;
