# RiskRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RiskRulesData]**](RiskRulesData.md) |  | [optional] 

## Example

```python
from conekta.models.risk_rules import RiskRules

# TODO update the JSON string below
json = "{}"
# create an instance of RiskRules from a JSON string
risk_rules_instance = RiskRules.from_json(json)
# print the JSON string representation of the object
print RiskRules.to_json()

# convert the object into a dict
risk_rules_dict = risk_rules_instance.to_dict()
# create an instance of RiskRules from a dict
risk_rules_form_dict = risk_rules.from_dict(risk_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


