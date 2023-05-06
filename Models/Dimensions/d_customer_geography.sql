
{{ config(materialized = 'table') }}

with d_customer_geography as (

    select ZIPCODE, STATE_ABBR, STATE, COUNTY, CITY
    from {{source('raw_data_1', 'CUSTOMER_GEOGRAPHY_DATA')}} 

),

final as(

    select * from d_customer_geography
)

select * from final
