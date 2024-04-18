# CreateRiskRulesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the rule | 
**var_field** | **str** | Field to be used for the rule | 
**value** | **str** | Value to be used for the rule | 

## Example

```python
from conekta.models.create_risk_rules_data import CreateRiskRulesData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRiskRulesData from a JSON string
create_risk_rules_data_instance = CreateRiskRulesData.from_json(json)
# print the JSON string representation of the object
print(CreateRiskRulesData.to_json())

# convert the object into a dict
create_risk_rules_data_dict = create_risk_rules_data_instance.to_dict()
# create an instance of CreateRiskRulesData from a dict
create_risk_rules_data_from_dict = CreateRiskRulesData.from_dict(create_risk_rules_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


