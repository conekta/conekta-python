# ShippingOrderResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Shipping amount in cents | 
**carrier** | **str** | Carrier name for the shipment | [optional] 
**tracking_number** | **str** | Tracking number can be used to track the shipment | [optional] 
**method** | **str** | Method of shipment | [optional] 
**metadata** | **Dict[str, object]** | Hash where the user can send additional information for each &#39;shipping&#39;. | [optional] 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from conekta.models.shipping_order_response import ShippingOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingOrderResponse from a JSON string
shipping_order_response_instance = ShippingOrderResponse.from_json(json)
# print the JSON string representation of the object
print ShippingOrderResponse.to_json()

# convert the object into a dict
shipping_order_response_dict = shipping_order_response_instance.to_dict()
# create an instance of ShippingOrderResponse from a dict
shipping_order_response_form_dict = shipping_order_response.from_dict(shipping_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


