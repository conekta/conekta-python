# ApiKeyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the api key is active | 
**description** | **str** | Detail of the use that will be given to the api key | 
**role** | **str** |  | 

## Example

```python
from conekta.models.api_key_request import ApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyRequest from a JSON string
api_key_request_instance = ApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print ApiKeyRequest.to_json()

# convert the object into a dict
api_key_request_dict = api_key_request_instance.to_dict()
# create an instance of ApiKeyRequest from a dict
api_key_request_form_dict = api_key_request.from_dict(api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


