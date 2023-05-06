
{{ config(materialized='table') }}

with d_product as (

    select product_id, product_name, category_id
    from {{source('raw_data_1', 'PRODUCT')}}
),

final as (

    select * from d_product
)

select* from final

