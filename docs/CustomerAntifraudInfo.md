# CustomerAntifraudInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_created_at** | **int** |  | [optional] 
**first_paid_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.customer_antifraud_info import CustomerAntifraudInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAntifraudInfo from a JSON string
customer_antifraud_info_instance = CustomerAntifraudInfo.from_json(json)
# print the JSON string representation of the object
print CustomerAntifraudInfo.to_json()

# convert the object into a dict
customer_antifraud_info_dict = customer_antifraud_info_instance.to_dict()
# create an instance of CustomerAntifraudInfo from a dict
customer_antifraud_info_form_dict = customer_antifraud_info.from_dict(customer_antifraud_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


