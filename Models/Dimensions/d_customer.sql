
{{ config(materialized='table') }}

with d_customer as (

    select CUSTOMER_ID, CUSTOMER_NAME, ZIP_CODE
    from {{source('raw_data_1', 'CUSTOMER')}}

),

final as (

    select * from d_customer
)

select * from final
