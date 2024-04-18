# UpdateCustomerAntifraudInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_created_at** | **int** |  | [optional] 
**first_paid_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.update_customer_antifraud_info import UpdateCustomerAntifraudInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerAntifraudInfo from a JSON string
update_customer_antifraud_info_instance = UpdateCustomerAntifraudInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerAntifraudInfo.to_json())

# convert the object into a dict
update_customer_antifraud_info_dict = update_customer_antifraud_info_instance.to_dict()
# create an instance of UpdateCustomerAntifraudInfo from a dict
update_customer_antifraud_info_from_dict = UpdateCustomerAntifraudInfo.from_dict(update_customer_antifraud_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


