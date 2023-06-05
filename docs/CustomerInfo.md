# CustomerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**corporate** | **bool** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from conekta.models.customer_info import CustomerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInfo from a JSON string
customer_info_instance = CustomerInfo.from_json(json)
# print the JSON string representation of the object
print CustomerInfo.to_json()

# convert the object into a dict
customer_info_dict = customer_info_instance.to_dict()
# create an instance of CustomerInfo from a dict
customer_info_form_dict = customer_info.from_dict(customer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


