# OrderUpdateCustomerInfo


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
from conekta.models.order_update_customer_info import OrderUpdateCustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdateCustomerInfo from a JSON string
order_update_customer_info_instance = OrderUpdateCustomerInfo.from_json(json)
# print the JSON string representation of the object
print(OrderUpdateCustomerInfo.to_json())

# convert the object into a dict
order_update_customer_info_dict = order_update_customer_info_instance.to_dict()
# create an instance of OrderUpdateCustomerInfo from a dict
order_update_customer_info_from_dict = OrderUpdateCustomerInfo.from_dict(order_update_customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


