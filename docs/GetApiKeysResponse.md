# GetApiKeysResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**data** | [**List[ApiKeyResponse]**](ApiKeyResponse.md) |  | [optional] 

## Example

```python
from conekta.models.get_api_keys_response import GetApiKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiKeysResponse from a JSON string
get_api_keys_response_instance = GetApiKeysResponse.from_json(json)
# print the JSON string representation of the object
print GetApiKeysResponse.to_json()

# convert the object into a dict
get_api_keys_response_dict = get_api_keys_response_instance.to_dict()
# create an instance of GetApiKeysResponse from a dict
get_api_keys_response_form_dict = get_api_keys_response.from_dict(get_api_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


