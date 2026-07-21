# LogsResponseForRequest

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
from conekta.models.logs_response_for_request import LogsResponseForRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogsResponseForRequest from a JSON string
logs_response_for_request_instance = LogsResponseForRequest.from_json(json)
# print the JSON string representation of the object
print(LogsResponseForRequest.to_json())

# convert the object into a dict
logs_response_for_request_dict = logs_response_for_request_instance.to_dict()
# create an instance of LogsResponseForRequest from a dict
logs_response_for_request_from_dict = LogsResponseForRequest.from_dict(logs_response_for_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


