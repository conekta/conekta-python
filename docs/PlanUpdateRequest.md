# PlanUpdateRequest

a plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount in cents that will be charged on the interval specified. | [optional] 
**currency** | **str** | ISO 4217 for currencies, for the Mexican peso it is MXN/USD | [optional] 
**expiry_count** | **int** | Number of repetitions of the frequency NUMBER OF CHARGES TO BE MADE, considering the interval and frequency, this evolves over time, but is subject to the expiration count. | [optional] 
**name** | **str** | The name of the plan. | [optional] 

## Example

```python
from conekta.models.plan_update_request import PlanUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanUpdateRequest from a JSON string
plan_update_request_instance = PlanUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PlanUpdateRequest.to_json())

# convert the object into a dict
plan_update_request_dict = plan_update_request_instance.to_dict()
# create an instance of PlanUpdateRequest from a dict
plan_update_request_from_dict = PlanUpdateRequest.from_dict(plan_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


