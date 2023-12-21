# OrderResponseCustomerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**customer_custom_reference** | **str** | Custom reference | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**corporate** | **bool** |  | [optional] [default to False]
**customer_id** | **str** |  | [optional] 

## Example

```python
from conekta.models.order_response_customer_info import OrderResponseCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseCustomerInfo from a JSON string
order_response_customer_info_instance = OrderResponseCustomerInfo.from_json(json)
# print the JSON string representation of the object
print OrderResponseCustomerInfo.to_json()

# convert the object into a dict
order_response_customer_info_dict = order_response_customer_info_instance.to_dict()
# create an instance of OrderResponseCustomerInfo from a dict
order_response_customer_info_form_dict = order_response_customer_info.from_dict(order_response_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


