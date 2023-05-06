
{{ config(
          materialized='incremental',
          unique_key='ORDER_DATE'
) }}

with f_order as (

    select o.order_id, c.customer_id, o.product_id, o.unit_price, o.quantity, o.discount, o.total_price, c.ORDER_DATE
    from {{source('raw_data_1', 'ORDER_DETAILS')}} o
    left join {{source('raw_data_1', 'CUSTOMER_ORDER')}} c
    on c.order_id=o.order_id

{% if is_incremental() %}

  where ORDER_DATE > (select max(ORDER_DATE) from {{ this }})

{% endif %}

),

final as (

    select * from f_order
)

select * from final
