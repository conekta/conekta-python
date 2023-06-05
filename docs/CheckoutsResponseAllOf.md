# CheckoutsResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CheckoutResponse]**](CheckoutResponse.md) |  | [optional] 

## Example

```python
from conekta.models.checkouts_response_all_of import CheckoutsResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutsResponseAllOf from a JSON string
checkouts_response_all_of_instance = CheckoutsResponseAllOf.from_json(json)
# print the JSON string representation of the object
print CheckoutsResponseAllOf.to_json()

# convert the object into a dict
checkouts_response_all_of_dict = checkouts_response_all_of_instance.to_dict()
# create an instance of CheckoutsResponseAllOf from a dict
checkouts_response_all_of_form_dict = checkouts_response_all_of.from_dict(checkouts_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


