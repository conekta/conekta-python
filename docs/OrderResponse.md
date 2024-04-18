# OrderResponse

order response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The total amount to be collected in cents | [optional] 
**amount_refunded** | **int** | The total amount refunded in cents | [optional] 
**channel** | [**ChargeResponseChannel**](ChargeResponseChannel.md) |  | [optional] 
**charges** | [**OrderResponseCharges**](OrderResponseCharges.md) |  | [optional] 
**checkout** | [**OrderResponseCheckout**](OrderResponseCheckout.md) |  | [optional] 
**created_at** | **int** | The time at which the object was created in seconds since the Unix epoch | [optional] 
**currency** | **str** | The three-letter ISO 4217 currency code. The currency of the order. | [optional] 
**customer_info** | [**OrderResponseCustomerInfo**](OrderResponseCustomerInfo.md) |  | [optional] 
**discount_lines** | [**OrderResponseDiscountLines**](OrderResponseDiscountLines.md) |  | [optional] 
**fiscal_entity** | [**OrderFiscalEntityResponse**](OrderFiscalEntityResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 
**is_refundable** | **bool** |  | [optional] 
**line_items** | [**OrderResponseProducts**](OrderResponseProducts.md) |  | [optional] 
**livemode** | **bool** | Whether the object exists in live mode or test mode | [optional] 
**metadata** | **Dict[str, object]** | Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. | [optional] 
**next_action** | [**OrderNextActionResponse**](OrderNextActionResponse.md) |  | [optional] 
**object** | **str** | String representing the object’s type. Objects of the same type share the same value. | [optional] 
**payment_status** | **str** | The payment status of the order. | [optional] 
**processing_mode** | **str** | Indicates the processing mode for the order, either ecommerce, recurrent or validation. | [optional] 
**shipping_contact** | [**OrderResponseShippingContact**](OrderResponseShippingContact.md) |  | [optional] 
**updated_at** | **int** | The time at which the object was last updated in seconds since the Unix epoch | [optional] 

## Example

```python
from conekta.models.order_response import OrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponse from a JSON string
order_response_instance = OrderResponse.from_json(json)
# print the JSON string representation of the object
print(OrderResponse.to_json())

# convert the object into a dict
order_response_dict = order_response_instance.to_dict()
# create an instance of OrderResponse from a dict
order_response_from_dict = OrderResponse.from_dict(order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


