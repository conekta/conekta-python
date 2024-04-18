# ShippingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Shipping amount in cents | 
**carrier** | **str** | Carrier name for the shipment | [optional] 
**tracking_number** | **str** | Tracking number can be used to track the shipment | [optional] 
**method** | **str** | Method of shipment | [optional] 
**metadata** | **Dict[str, object]** | Hash where the user can send additional information for each &#39;shipping&#39;. | [optional] 

## Example

```python
from conekta.models.shipping_request import ShippingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingRequest from a JSON string
shipping_request_instance = ShippingRequest.from_json(json)
# print the JSON string representation of the object
print(ShippingRequest.to_json())

# convert the object into a dict
shipping_request_dict = shipping_request_instance.to_dict()
# create an instance of ShippingRequest from a dict
shipping_request_from_dict = ShippingRequest.from_dict(shipping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


