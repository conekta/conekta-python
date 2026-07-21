# CreateRuleWhitelistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the rule | 
**var_field** | **str** | Field to be used for the rule | 
**value** | **str** | Value to be used for the rule | 

## Example

```python
from conekta.models.create_rule_whitelist_request import CreateRuleWhitelistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRuleWhitelistRequest from a JSON string
create_rule_whitelist_request_instance = CreateRuleWhitelistRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRuleWhitelistRequest.to_json())

# convert the object into a dict
create_rule_whitelist_request_dict = create_rule_whitelist_request_instance.to_dict()
# create an instance of CreateRuleWhitelistRequest from a dict
create_rule_whitelist_request_from_dict = CreateRuleWhitelistRequest.from_dict(create_rule_whitelist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


