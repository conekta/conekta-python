# ApiKeyCreateResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_token** | **str** | It is occupied as a user when authenticated with basic authentication, with a blank password. This value will only appear once, in the request to create a new key | [optional] 

## Example

```python
from conekta.models.api_key_create_response_all_of import ApiKeyCreateResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreateResponseAllOf from a JSON string
api_key_create_response_all_of_instance = ApiKeyCreateResponseAllOf.from_json(json)
# print the JSON string representation of the object
print ApiKeyCreateResponseAllOf.to_json()

# convert the object into a dict
api_key_create_response_all_of_dict = api_key_create_response_all_of_instance.to_dict()
# create an instance of ApiKeyCreateResponseAllOf from a dict
api_key_create_response_all_of_form_dict = api_key_create_response_all_of.from_dict(api_key_create_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


