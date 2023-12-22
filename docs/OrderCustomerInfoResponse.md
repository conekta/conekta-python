# OrderCustomerInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_custom_reference** | **str** | Custom reference | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**corporate** | **bool** |  | [optional] [default to False]
**object** | **str** |  | [optional] 

## Example

```python
from conekta.models.order_customer_info_response import OrderCustomerInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCustomerInfoResponse from a JSON string
order_customer_info_response_instance = OrderCustomerInfoResponse.from_json(json)
# print the JSON string representation of the object
print OrderCustomerInfoResponse.to_json()

# convert the object into a dict
order_customer_info_response_dict = order_customer_info_response_instance.to_dict()
# create an instance of OrderCustomerInfoResponse from a dict
order_customer_info_response_form_dict = order_customer_info_response.from_dict(order_customer_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


