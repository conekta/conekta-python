# CustomerAntifraudInfoResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_paid_at** | **int** |  | [optional] 
**account_created_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.customer_antifraud_info_response import CustomerAntifraudInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAntifraudInfoResponse from a JSON string
customer_antifraud_info_response_instance = CustomerAntifraudInfoResponse.from_json(json)
# print the JSON string representation of the object
print CustomerAntifraudInfoResponse.to_json()

# convert the object into a dict
customer_antifraud_info_response_dict = customer_antifraud_info_response_instance.to_dict()
# create an instance of CustomerAntifraudInfoResponse from a dict
customer_antifraud_info_response_form_dict = customer_antifraud_info_response.from_dict(customer_antifraud_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


