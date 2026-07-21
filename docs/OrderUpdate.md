# OrderUpdate

a order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges** | [**List[ChargeRequest]**](ChargeRequest.md) |  | [optional] 
**checkout** | [**OrderCheckoutRequest**](OrderCheckoutRequest.md) |  | [optional] 
**currency** | **str** | Currency with which the payment will be made. It uses the 3-letter code of the [International Standard ISO 4217.](https://es.wikipedia.org/wiki/ISO_4217) | [optional] 
**customer_info** | [**OrderUpdateCustomerInfo**](OrderUpdateCustomerInfo.md) |  | [optional] 
**discount_lines** | [**List[OrderDiscountLinesRequest]**](OrderDiscountLinesRequest.md) | List of [discounts](https://developers.conekta.com/v2.2.0/reference/orderscreatediscountline) that are applied to the order. | [optional] 
**fiscal_entity** | [**OrderUpdateFiscalEntityRequest**](OrderUpdateFiscalEntityRequest.md) |  | [optional] 
**line_items** | [**List[Product]**](Product.md) | List of [products](https://developers.conekta.com/v2.2.0/reference/orderscreateproduct) that are sold in the order. You must have at least one product. | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**pre_authorize** | **bool** | Indicates whether the order charges must be preauthorized | [optional] 
**shipping_contact** | [**CustomerShippingContactsRequest**](CustomerShippingContactsRequest.md) |  | [optional] 
**shipping_lines** | [**List[ShippingRequest]**](ShippingRequest.md) | List of [shipping costs](https://developers.conekta.com/v2.2.0/reference/orderscreateshipping). If the online store offers digital products. | [optional] 
**tax_lines** | [**List[OrderTaxRequest]**](OrderTaxRequest.md) |  | [optional] 

## Example

```python
from conekta.models.order_update import OrderUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdate from a JSON string
order_update_instance = OrderUpdate.from_json(json)
# print the JSON string representation of the object
print(OrderUpdate.to_json())

# convert the object into a dict
order_update_dict = order_update_instance.to_dict()
# create an instance of OrderUpdate from a dict
order_update_from_dict = OrderUpdate.from_dict(order_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


