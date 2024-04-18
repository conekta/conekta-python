# ApiKeyResponseOnDelete

api keys model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the api key is active | [optional] 
**created_at** | **int** | Unix timestamp in seconds of when the api key was created | [optional] 
**description** | **str** | A name or brief explanation of what this api key is used for | [optional] 
**livemode** | **bool** | Indicates if the api key is in production | [optional] 
**prefix** | **str** | The first few characters of the authentication_token | [optional] 
**id** | **str** | Unique identifier of the api key | [optional] 
**object** | **str** | Object name, value is &#39;api_key&#39; | [optional] 
**deleted** | **bool** | Indicates if the api key was deleted | [optional] 
**role** | **str** | Indicates if the api key is private or public | [optional] 

## Example

```python
from conekta.models.api_key_response_on_delete import ApiKeyResponseOnDelete

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResponseOnDelete from a JSON string
api_key_response_on_delete_instance = ApiKeyResponseOnDelete.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResponseOnDelete.to_json())

# convert the object into a dict
api_key_response_on_delete_dict = api_key_response_on_delete_instance.to_dict()
# create an instance of ApiKeyResponseOnDelete from a dict
api_key_response_on_delete_from_dict = ApiKeyResponseOnDelete.from_dict(api_key_response_on_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


