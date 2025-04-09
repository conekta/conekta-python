# PlanRequest

a plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount in cents that will be charged on the interval specified. | 
**currency** | **str** | ISO 4217 for currencies, for the Mexican peso it is MXN/USD | [optional] 
**expiry_count** | **int** | Number of repetitions of the frequency NUMBER OF CHARGES TO BE MADE, considering the interval and frequency, this evolves over time, but is subject to the expiration count. | [optional] 
**frequency** | **int** | Frequency of the charge, which together with the interval, can be every 3 weeks, every 4 months, every 2 years, every 5 fortnights | 
**id** | **str** | internal reference id | [optional] 
**interval** | **str** | The interval of time between each charge. | 
**name** | **str** | The name of the plan. | 
**trial_period_days** | **int** | The number of days the customer will have a free trial. | [optional] 
**max_retries** | **int** | (optional) Specifies the maximum number of retry attempts for a subscription payment before it is canceled. | [optional] 
**retry_delay_hours** | **int** | (optional)  Defines the number of hours between subscription payment retry attempts. | [optional] 

## Example

```python
from conekta.models.plan_request import PlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanRequest from a JSON string
plan_request_instance = PlanRequest.from_json(json)
# print the JSON string representation of the object
print(PlanRequest.to_json())

# convert the object into a dict
plan_request_dict = plan_request_instance.to_dict()
# create an instance of PlanRequest from a dict
plan_request_from_dict = PlanRequest.from_dict(plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


