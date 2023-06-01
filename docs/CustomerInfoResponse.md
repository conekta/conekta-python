# CustomerInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**corporate** | **bool** |  | [optional] [default to False]
**object** | **str** |  | [optional] 

## Example

```python
from conekta.models.customer_info_response import CustomerInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInfoResponse from a JSON string
customer_info_response_instance = CustomerInfoResponse.from_json(json)
# print the JSON string representation of the object
print CustomerInfoResponse.to_json()

# convert the object into a dict
customer_info_response_dict = customer_info_response_instance.to_dict()
# create an instance of CustomerInfoResponse from a dict
customer_info_response_form_dict = customer_info_response.from_dict(customer_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


