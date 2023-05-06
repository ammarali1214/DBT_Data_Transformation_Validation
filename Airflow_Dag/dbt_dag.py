# 1. Import modules
from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.models import Variable
from airflow_dbt.operators.dbt_operator import (DbtRunOperator, DbtTestOperator)


# 2. Define default arguments
default_args = {
    
    'owner': 'Ammar',
    'start_date': datetime(2023,4,30)
    }


# 3. Instantiate the DAG
dag = DAG (
        dag_id = 'dbt_DAG',
        default_args = default_args,
        schedule= '@once'
        )


# 4.Define tasks

# start_task is defined to make sure if DAG is started successfully
start_task = EmptyOperator(
        task_id = 'start',
        dag = dag
        )


# task_mysql_sf task is defined to trigger Airbyte Connection of MySQL <--> Snowflake to extract and load Data from MySQL to Snowflake
task_mysql_sf = AirbyteTriggerSyncOperator(
        task_id = 'mysql_snowflake_sync', 
        airbyte_conn_id = 'airflow_airbyte', 
        connection_id = '7f948beb-2a0f-4532-97fc-3a80ab65e589',
        asynchronous = False,
        dag = dag
        )                                                       


# task_API1_sf task is defined to trigger Airbyte Connection of File <--> Snowflake to extract and load Data from REST API to Snowflake  
task_API1_sf = AirbyteTriggerSyncOperator(
        task_id = 'REST_API_Online_Shop_API', 
        airbyte_conn_id = 'airflow_airbyte', 
        connection_id = 'da283507-c066-4d19-b8b8-21ebf66601a4',
        asynchronous = False,
        dag = dag
        )


# task_API2_sf task is defined to trigger Airbyte Connection of File <--> Snowflake to extract and load Data from REST API to Snowflake  
task_API2_sf = AirbyteTriggerSyncOperator(
        task_id = 'REST_API_Geography_API', 
        airbyte_conn_id = 'airflow_airbyte', 
        connection_id = '724ab7ff-e841-4350-93b4-cbe3927d1bc9', 
        asynchronous = False,
        dag = dag
        )


# dbt_run_task is defined to execute the models - it'll execute "dbt run" command.
dbt_run_task = DbtRunOperator(
        task_id = 'dbt_run',
        project_dir = Variable.get('project_dir'),
        target = Variable.get('exec_env'),
        dag = dag
        )


# dbt_test_task is defined to execute the tests defined for the models - it'll execute "dbt test" command.
dbt_test_task = DbtTestOperator(
        task_id = 'dbt_test',
        project_dir = Variable.get('project_dir'),
        target = Variable.get('exec_env'),
        dag = dag
        )

# end_task is defined to make sure if DAG has ended successfully
end_task = EmptyOperator(
        task_id = 'end',
        dag = dag
        )

# 5.Define dependencies
start_task >> [task_mysql_sf, task_API1_sf, task_API2_sf] >> dbt_run_task>> dbt_test_task>> end_task
