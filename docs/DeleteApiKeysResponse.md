# DeleteApiKeysResponse


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
**deleted** | **bool** |  | [optional] 
**role** | **str** | Indicates if the api key is private or public | [optional] 

## Example

```python
from conekta.models.delete_api_keys_response import DeleteApiKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApiKeysResponse from a JSON string
delete_api_keys_response_instance = DeleteApiKeysResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteApiKeysResponse.to_json())

# convert the object into a dict
delete_api_keys_response_dict = delete_api_keys_response_instance.to_dict()
# create an instance of DeleteApiKeysResponse from a dict
delete_api_keys_response_from_dict = DeleteApiKeysResponse.from_dict(delete_api_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


