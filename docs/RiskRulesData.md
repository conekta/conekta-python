# RiskRulesData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | rule id | [optional] 
**field** | **str** | field to be used for the rule | [optional] 
**created_at** | **str** | rule creation date | [optional] 
**value** | **str** | value to be used for the rule | [optional] 
**is_global** | **bool** | if the rule is global | [optional] 
**is_test** | **bool** | if the rule is test | [optional] 
**description** | **str** | description of the rule | [optional] 

## Example

```python
from conekta.models.risk_rules_data import RiskRulesData

# TODO update the JSON string below
json = "{}"
# create an instance of RiskRulesData from a JSON string
risk_rules_data_instance = RiskRulesData.from_json(json)
# print the JSON string representation of the object
print RiskRulesData.to_json()

# convert the object into a dict
risk_rules_data_dict = risk_rules_data_instance.to_dict()
# create an instance of RiskRulesData from a dict
risk_rules_data_form_dict = risk_rules_data.from_dict(risk_rules_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


