# ChargebackFileResponse

A file associated with a chargeback (e.g. evidence document)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 

## Example

```python
from conekta.models.chargeback_file_response import ChargebackFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargebackFileResponse from a JSON string
chargeback_file_response_instance = ChargebackFileResponse.from_json(json)
# print the JSON string representation of the object
print(ChargebackFileResponse.to_json())

# convert the object into a dict
chargeback_file_response_dict = chargeback_file_response_instance.to_dict()
# create an instance of ChargebackFileResponse from a dict
chargeback_file_response_from_dict = ChargebackFileResponse.from_dict(chargeback_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


