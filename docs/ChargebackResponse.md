# ChargebackResponse

Chargeback object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**followup_status** | **str** |  | [optional] 
**response_from_client** | **str** |  | [optional] 
**files** | [**List[ChargebackFileResponse]**](ChargebackFileResponse.md) |  | [optional] 
**object** | **str** |  | [optional] 
**charge_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**evidence_due_by** | **int** |  | [optional] 

## Example

```python
from conekta.models.chargeback_response import ChargebackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChargebackResponse from a JSON string
chargeback_response_instance = ChargebackResponse.from_json(json)
# print the JSON string representation of the object
print(ChargebackResponse.to_json())

# convert the object into a dict
chargeback_response_dict = chargeback_response_instance.to_dict()
# create an instance of ChargebackResponse from a dict
chargeback_response_from_dict = ChargebackResponse.from_dict(chargeback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


