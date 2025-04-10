# PlanResponse

plans model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**created_at** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**expiry_count** | **int** |  | [optional] 
**frequency** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**livemode** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**trial_period_days** | **int** |  | [optional] 
**max_retries** | **int** |  | [optional] 
**retry_delay_hours** | **int** |  | [optional] 

## Example

```python
from conekta.models.plan_response import PlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponse from a JSON string
plan_response_instance = PlanResponse.from_json(json)
# print the JSON string representation of the object
print(PlanResponse.to_json())

# convert the object into a dict
plan_response_dict = plan_response_instance.to_dict()
# create an instance of PlanResponse from a dict
plan_response_from_dict = PlanResponse.from_dict(plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


