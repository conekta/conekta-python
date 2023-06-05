# DeleteApiKeysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the api key is active | [optional] 
**created_at** | **int** | Unix timestamp in seconds with the creation date of the api key | [optional] 
**description** | **str** | Detail of the use that will be given to the api key | [optional] 
**id** | **str** | Unique identifier of the api key | [optional] 
**livemode** | **bool** | Indicates if the api key is in live mode | [optional] 
**object** | **str** | Object name, value is api_key | [optional] 
**prefix** | **str** | The first few characters of the authentication_token | [optional] 
**role** | **str** | Indicates the user account private&#x3D;owner or public&#x3D;public | [optional] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from conekta.models.delete_api_keys_response import DeleteApiKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteApiKeysResponse from a JSON string
delete_api_keys_response_instance = DeleteApiKeysResponse.from_json(json)
# print the JSON string representation of the object
print DeleteApiKeysResponse.to_json()

# convert the object into a dict
delete_api_keys_response_dict = delete_api_keys_response_instance.to_dict()
# create an instance of DeleteApiKeysResponse from a dict
delete_api_keys_response_form_dict = delete_api_keys_response.from_dict(delete_api_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


