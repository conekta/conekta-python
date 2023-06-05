# DeletedBlacklistRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Blacklist rule id | [optional] 
**field** | **str** | field used for blacklists rule deleted | [optional] 
**value** | **str** | value used for blacklists rule deleted | [optional] 
**description** | **str** | use an description for blacklisted rule | [optional] 

## Example

```python
from conekta.models.deleted_blacklist_rule_response import DeletedBlacklistRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedBlacklistRuleResponse from a JSON string
deleted_blacklist_rule_response_instance = DeletedBlacklistRuleResponse.from_json(json)
# print the JSON string representation of the object
print DeletedBlacklistRuleResponse.to_json()

# convert the object into a dict
deleted_blacklist_rule_response_dict = deleted_blacklist_rule_response_instance.to_dict()
# create an instance of DeletedBlacklistRuleResponse from a dict
deleted_blacklist_rule_response_form_dict = deleted_blacklist_rule_response.from_dict(deleted_blacklist_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


