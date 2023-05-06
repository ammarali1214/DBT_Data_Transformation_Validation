### DBT_Data_Transformation_Validation

1 - .dbt folder contains profile.yml file

2 - Models folder contains generic test file named model_tests.yml and source file named stg_source.yml

2.1 - Models/Dimensions/ contains all models of dimensional tables

2.2 - Models/fact_folder/ contains all models of fact tables

2.3 - Models/aggs_folder/ contains the model of Aggregate Table

3 - tests folder contains singulat test of f_order_total_price_test.sql

4 - Airflow_Dag folder contains Airflow's dag file


