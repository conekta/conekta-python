# UpdatePlan

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
from conekta.models.update_plan import UpdatePlan

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlan from a JSON string
update_plan_instance = UpdatePlan.from_json(json)
# print the JSON string representation of the object
print(UpdatePlan.to_json())

# convert the object into a dict
update_plan_dict = update_plan_instance.to_dict()
# create an instance of UpdatePlan from a dict
update_plan_from_dict = UpdatePlan.from_dict(update_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


