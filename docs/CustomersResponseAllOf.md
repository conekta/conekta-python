# CustomersResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomerResponse]**](CustomerResponse.md) |  | [optional] 

## Example

```python
from conekta.models.customers_response_all_of import CustomersResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CustomersResponseAllOf from a JSON string
customers_response_all_of_instance = CustomersResponseAllOf.from_json(json)
# print the JSON string representation of the object
print CustomersResponseAllOf.to_json()

# convert the object into a dict
customers_response_all_of_dict = customers_response_all_of_instance.to_dict()
# create an instance of CustomersResponseAllOf from a dict
customers_response_all_of_form_dict = customers_response_all_of.from_dict(customers_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


