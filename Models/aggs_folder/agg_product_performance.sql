
{{ config(materialized='table') }}

with agg_product_performance AS (

    select f.product_id, p.category_id product_category_id, g.ZIPCODE state_cd, f.order_date day_date, count(f.order_id) total_orders, sum(f.total_price) total_revnue,  avg(cr.PRODUCT_REVIEW_SCORE) AVG_PROD_REVIEW_SCORE 
    from {{ref('f_order')}} f
    join {{ref('d_product')}} p on p.product_id = f.product_id 
    join {{ref('d_customer')}} dc on dc.customer_id=f.customer_id 
    join {{ref('d_customer_geography')}} g on dc.ZIP_CODE=g.ZIPCODE 
    join {{source('raw_data_1', 'CUSTOMER_REVIEWS_DATA')}} cr on cr.product_id=f.product_id 
    group by f.product_id, product_category_id, day_date, ZIPCODE
),

final as (

    select * from agg_product_performance
)

select * from final 

