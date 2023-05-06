
with f_order_total_price_test as (

    select * from {{ref('f_order')}}
)

select order_id, total_price
FROM f_order_total_price_test
where total_price <=0
