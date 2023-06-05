# GetApiKeysResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiKeyResponse]**](ApiKeyResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_api_keys_response_all_of import GetApiKeysResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiKeysResponseAllOf from a JSON string
get_api_keys_response_all_of_instance = GetApiKeysResponseAllOf.from_json(json)
# print the JSON string representation of the object
print GetApiKeysResponseAllOf.to_json()

# convert the object into a dict
get_api_keys_response_all_of_dict = get_api_keys_response_all_of_instance.to_dict()
# create an instance of GetApiKeysResponseAllOf from a dict
get_api_keys_response_all_of_form_dict = get_api_keys_response_all_of.from_dict(get_api_keys_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


