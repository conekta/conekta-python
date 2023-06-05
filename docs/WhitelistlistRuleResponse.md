# WhitelistlistRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Whitelist rule id | [optional] 
**field** | **str** | field used for whitelists rule | [optional] 
**value** | **str** | value used for whitelists rule | [optional] 
**description** | **str** | use an description for whitelisted rule | [optional] 

## Example

```python
from conekta.models.whitelistlist_rule_response import WhitelistlistRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistlistRuleResponse from a JSON string
whitelistlist_rule_response_instance = WhitelistlistRuleResponse.from_json(json)
# print the JSON string representation of the object
print WhitelistlistRuleResponse.to_json()

# convert the object into a dict
whitelistlist_rule_response_dict = whitelistlist_rule_response_instance.to_dict()
# create an instance of WhitelistlistRuleResponse from a dict
whitelistlist_rule_response_form_dict = whitelistlist_rule_response.from_dict(whitelistlist_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


