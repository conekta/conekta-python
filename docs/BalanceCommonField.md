# BalanceCommonField

balance common fields model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The balance&#39;s amount | [optional] 
**currency** | **str** | The balance&#39;s currency | [optional] 

## Example

```python
from conekta.models.balance_common_field import BalanceCommonField

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceCommonField from a JSON string
balance_common_field_instance = BalanceCommonField.from_json(json)
# print the JSON string representation of the object
print(BalanceCommonField.to_json())

# convert the object into a dict
balance_common_field_dict = balance_common_field_instance.to_dict()
# create an instance of BalanceCommonField from a dict
balance_common_field_from_dict = BalanceCommonField.from_dict(balance_common_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


