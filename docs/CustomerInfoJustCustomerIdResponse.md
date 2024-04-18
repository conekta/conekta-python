# CustomerInfoJustCustomerIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 

## Example

```python
from conekta.models.customer_info_just_customer_id_response import CustomerInfoJustCustomerIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInfoJustCustomerIdResponse from a JSON string
customer_info_just_customer_id_response_instance = CustomerInfoJustCustomerIdResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerInfoJustCustomerIdResponse.to_json())

# convert the object into a dict
customer_info_just_customer_id_response_dict = customer_info_just_customer_id_response_instance.to_dict()
# create an instance of CustomerInfoJustCustomerIdResponse from a dict
customer_info_just_customer_id_response_from_dict = CustomerInfoJustCustomerIdResponse.from_dict(customer_info_just_customer_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


