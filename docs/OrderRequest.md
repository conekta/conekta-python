# OrderRequest

a order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges** | [**List[ChargeRequest]**](ChargeRequest.md) | List of [charges](https://developers.conekta.com/v2.1.0/reference/orderscreatecharge) that are applied to the order | [optional] 
**checkout** | [**CheckoutRequest**](CheckoutRequest.md) |  | [optional] 
**currency** | **str** | Currency with which the payment will be made. It uses the 3-letter code of the [International Standard ISO 4217.](https://es.wikipedia.org/wiki/ISO_4217) | 
**customer_info** | [**OrderRequestCustomerInfo**](OrderRequestCustomerInfo.md) |  | 
**discount_lines** | [**List[OrderDiscountLinesRequest]**](OrderDiscountLinesRequest.md) | List of [discounts](https://developers.conekta.com/v2.1.0/reference/orderscreatediscountline) that are applied to the order. You must have at least one discount. | [optional] 
**line_items** | [**List[Product]**](Product.md) | List of [products](https://developers.conekta.com/v2.1.0/reference/orderscreateproduct) that are sold in the order. You must have at least one product. | 
**metadata** | **Dict[str, object]** |  | [optional] 
**needs_shipping_contact** | **bool** | Allows you to fill out the shipping information at checkout | [optional] 
**pre_authorize** | **bool** | Indicates whether the order charges must be preauthorized | [optional] [default to False]
**shipping_contact** | [**CustomerShippingContacts**](CustomerShippingContacts.md) |  | [optional] 
**shipping_lines** | [**List[ShippingRequest]**](ShippingRequest.md) | List of [shipping costs](https://developers.conekta.com/v2.1.0/reference/orderscreateshipping). If the online store offers digital products. | [optional] 
**tax_lines** | [**List[OrderTaxRequest]**](OrderTaxRequest.md) | List of [taxes](https://developers.conekta.com/v2.1.0/reference/orderscreatetaxes) that are applied to the order. | [optional] 

## Example

```python
from conekta.models.order_request import OrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderRequest from a JSON string
order_request_instance = OrderRequest.from_json(json)
# print the JSON string representation of the object
print OrderRequest.to_json()

# convert the object into a dict
order_request_dict = order_request_instance.to_dict()
# create an instance of OrderRequest from a dict
order_request_form_dict = order_request.from_dict(order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


