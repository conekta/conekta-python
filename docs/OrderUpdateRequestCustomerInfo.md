# OrderUpdateRequestCustomerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**corporate** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 
**customer_id** | **str** |  | 

## Example

```python
from conekta.models.order_update_request_customer_info import OrderUpdateRequestCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdateRequestCustomerInfo from a JSON string
order_update_request_customer_info_instance = OrderUpdateRequestCustomerInfo.from_json(json)
# print the JSON string representation of the object
print OrderUpdateRequestCustomerInfo.to_json()

# convert the object into a dict
order_update_request_customer_info_dict = order_update_request_customer_info_instance.to_dict()
# create an instance of OrderUpdateRequestCustomerInfo from a dict
order_update_request_customer_info_form_dict = order_update_request_customer_info.from_dict(order_update_request_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


