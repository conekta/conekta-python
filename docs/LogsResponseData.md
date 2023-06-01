# LogsResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
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
from conekta.models.logs_response_data import LogsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of LogsResponseData from a JSON string
logs_response_data_instance = LogsResponseData.from_json(json)
# print the JSON string representation of the object
print LogsResponseData.to_json()

# convert the object into a dict
logs_response_data_dict = logs_response_data_instance.to_dict()
# create an instance of LogsResponseData from a dict
logs_response_data_form_dict = logs_response_data.from_dict(logs_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


