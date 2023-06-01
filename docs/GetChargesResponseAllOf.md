# GetChargesResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ChargeResponse]**](ChargeResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_charges_response_all_of import GetChargesResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesResponseAllOf from a JSON string
get_charges_response_all_of_instance = GetChargesResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetChargesResponseAllOf.to_json()

# convert the object into a dict
get_charges_response_all_of_dict = get_charges_response_all_of_instance.to_dict()
# create an instance of GetChargesResponseAllOf from a dict
get_charges_response_all_of_form_dict = get_charges_response_all_of.from_dict(get_charges_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


