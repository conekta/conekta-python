# DeletedWhitelistRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Whitelist rule id | [optional] 
**field** | **str** | field used for whitelists rule deleted | [optional] 
**value** | **str** | value used for whitelists rule deleted | [optional] 
**description** | **str** | use an description for whitelisted rule | [optional] 

## Example

```python
from conekta.models.deleted_whitelist_rule_response import DeletedWhitelistRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedWhitelistRuleResponse from a JSON string
deleted_whitelist_rule_response_instance = DeletedWhitelistRuleResponse.from_json(json)
# print the JSON string representation of the object
print DeletedWhitelistRuleResponse.to_json()

# convert the object into a dict
deleted_whitelist_rule_response_dict = deleted_whitelist_rule_response_instance.to_dict()
# create an instance of DeletedWhitelistRuleResponse from a dict
deleted_whitelist_rule_response_form_dict = deleted_whitelist_rule_response.from_dict(deleted_whitelist_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


