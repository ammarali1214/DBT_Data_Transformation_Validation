
{{ config(materialized='table') }}

with d_product_category as (

    select category_id, category_name 
    from {{source('raw_data_1', 'PROD_CATEGORY')}}
),

final as (

    select * from d_product_category
)

select * from final

