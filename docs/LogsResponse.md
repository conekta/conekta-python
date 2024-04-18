# LogsResponse

logs model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | True, if there are more pages. | [optional] [readonly] 
**object** | **str** | The object type | [optional] [readonly] 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[LogsResponseData]**](LogsResponseData.md) | set to page results. | [optional] 

## Example

```python
from conekta.models.logs_response import LogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogsResponse from a JSON string
logs_response_instance = LogsResponse.from_json(json)
# print the JSON string representation of the object
print(LogsResponse.to_json())

# convert the object into a dict
logs_response_dict = logs_response_instance.to_dict()
# create an instance of LogsResponse from a dict
logs_response_from_dict = LogsResponse.from_dict(logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


