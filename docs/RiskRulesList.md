# RiskRulesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | Indicates if there are more pages to be requested | 
**object** | **str** | Object type, in this case is list | 
**next_page_url** | **str** | URL of the next page. | [optional] 
**previous_page_url** | **str** | Url of the previous page. | [optional] 
**data** | [**List[RiskRulesData]**](RiskRulesData.md) |  | [optional] 

## Example

```python
from conekta.models.risk_rules_list import RiskRulesList

# TODO update the JSON string below
json = "{}"
# create an instance of RiskRulesList from a JSON string
risk_rules_list_instance = RiskRulesList.from_json(json)
# print the JSON string representation of the object
print(RiskRulesList.to_json())

# convert the object into a dict
risk_rules_list_dict = risk_rules_list_instance.to_dict()
# create an instance of RiskRulesList from a dict
risk_rules_list_from_dict = RiskRulesList.from_dict(risk_rules_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


