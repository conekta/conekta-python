# BlacklistRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Blacklist rule id | [optional] 
**var_field** | **str** | field used for blacklists rule | [optional] 
**value** | **str** | value used for blacklists rule | [optional] 
**description** | **str** | use an description for blacklisted rule | [optional] 

## Example

```python
from conekta.models.blacklist_rule_response import BlacklistRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlacklistRuleResponse from a JSON string
blacklist_rule_response_instance = BlacklistRuleResponse.from_json(json)
# print the JSON string representation of the object
print(BlacklistRuleResponse.to_json())

# convert the object into a dict
blacklist_rule_response_dict = blacklist_rule_response_instance.to_dict()
# create an instance of BlacklistRuleResponse from a dict
blacklist_rule_response_from_dict = BlacklistRuleResponse.from_dict(blacklist_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


