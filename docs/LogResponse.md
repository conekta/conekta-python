# LogResponse

log model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | 
**id** | **str** |  | 
**ip_address** | **str** |  | [optional] 
**livemode** | **bool** |  | 
**loggable_id** | **str** |  | [optional] 
**loggable_type** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**oauth_token_id** | **str** |  | [optional] 
**query_string** | **Dict[str, object]** |  | [optional] 
**related** | **str** |  | [optional] 
**request_body** | **object** |  | [optional] 
**request_headers** | **Dict[str, str]** |  | [optional] 
**response_body** | **object** |  | [optional] 
**response_headers** | **Dict[str, str]** |  | [optional] 
**searchable_tags** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_account_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from conekta.models.log_response import LogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogResponse from a JSON string
log_response_instance = LogResponse.from_json(json)
# print the JSON string representation of the object
print LogResponse.to_json()

# convert the object into a dict
log_response_dict = log_response_instance.to_dict()
# create an instance of LogResponse from a dict
log_response_form_dict = log_response.from_dict(log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


